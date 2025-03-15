import torch
import torch.nn as nn
from torchvision.models import resnet18
from loguru import logger


class LicensePlateCTC(nn.Module):
    def __init__(self, num_classes, max_length=9):
        super().__init__()
        self.backbone = resnet18(pretrained=False)
        self.backbone = nn.Sequential(*list(self.backbone.children())[:-2])
        self.adaptive_pool = nn.AdaptiveAvgPool2d((1, max_length * 2))
        self.classifier = nn.Conv2d(512, num_classes + 1, kernel_size=1)

    def forward(self, x):
        x = self.backbone(x)
        x = self.adaptive_pool(x)
        x = self.classifier(x).squeeze(2)
        return x.permute(2, 0, 1)

def load_model(weights_path, num_classes, device):
    try:
        model = LicensePlateCTC(num_classes)
        state_dict = torch.load(weights_path, map_location=device)
        model.load_state_dict(state_dict)
        model.eval()
        logger.info(f"Model loaded successfully from {weights_path} on {device}")
        return model.to(device)
    except Exception as e:
        logger.error(f"Failed to load model from {weights_path}: {str(e)}", exc_info=True)
        raise
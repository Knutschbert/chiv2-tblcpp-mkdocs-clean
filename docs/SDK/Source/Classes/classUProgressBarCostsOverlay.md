---
title: UProgressBarCostsOverlay
type: class
aliases: UProgressBarCostsOverlay
share: false

---

# UProgressBarCostsOverlay





Inherits from UProgressBar

## Public Functions

|                | Name           |
| -------------- | -------------- |
| UMaterialInstanceDynamic * | **[[GetFillDynamicMaterial]]**() |
| void | **[[SetDamageFillColorAndOpacity]]**(FLinearColor InColor) |
| void | **[[SetOverlayFillColorAndOpacity]]**(FLinearColor InColor) |
| void | **[[SetOverlayPercent]]**(float InOverlayPercent) |
| | **[[UProgressBarCostsOverlay]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FSlateColor | **[[DamageFillColorAndOpacity]]**  |
| UWidget::FGetSlateColor | **[[DamageFillColorAndOpacityDelegate]]**  |
| FSlateBrush | **[[DamageFillImage]]**  |
| float | **[[DamageLingerTime]]**  |
| float | **[[DamageRemovedPerSecond]]**  |
| FSlateColor | **[[OverlayFillColorAndOpacity]]**  |
| UWidget::FGetSlateColor | **[[OverlayFillColorAndOpacityDelegate]]**  |
| FSlateBrush | **[[OverlayFillImage]]**  |
| float | **[[OverlayPercent]]**  |
| UWidget::FGetFloat | **[[OverlayPercentDelegate]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
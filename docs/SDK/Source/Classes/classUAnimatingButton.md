---
title: UAnimatingButton
type: class
aliases: UAnimatingButton
share: false

---

# UAnimatingButton





Inherits from UWidget

## Public Functions

|                | Name           |
| -------------- | -------------- |
| UMaterialInstanceDynamic * | **[[GetDynamicMaterial]]**() |
| void | **[[PlayNormalAnimation]]**() |
| void | **[[SetColorAndOpacity]]**(FLinearColor InColorAndOpacity) |
| | **[[UAnimatingButton]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [FTBLButtonAnimation](/docs/SDK/Source/Classes/structFTBLButtonAnimation.md) > | **[[Animations]]**  |
| FLinearColor | **[[ColorAndOpacity]]**  |
| UMaterialInterface * | **[[Material]]**  |
| FOnButtonClickedEvent | **[[OnClicked]]**  |
| FOnButtonDoubleClickEvent | **[[OnDoubleClick]]**  |
| FOnButtonHoverEvent | **[[OnHovered]]**  |
| FMouseClickWidget | **[[OnMouseClickWidgetEvent]]**  |
| FOnMouseDoubleClickWidget | **[[OnMouseDoubleClickWidgetEvent]]**  |
| FMouseEnterWidget | **[[OnMouseEnterWidgetEvent]]**  |
| FMouseLeaveWidget | **[[OnMouseLeaveWidgetEvent]]**  |
| FMouseReleaseWidget | **[[OnMouseReleaseWidgetEvent]]**  |
| FOverrideMaterial | **[[OnOverrideMaterialEvent]]**  |
| FOnButtonReleasedEvent | **[[OnReleased]]**  |
| FOnButtonHoverEvent | **[[OnUnhovered]]**  |
| TEnumAsByte< ETextJustify::Type > | **[[TextBlockJustification]]**  |
| FMargin | **[[TextBlockMargin]]**  |
| FTextBlockStyle | **[[TextBlockStyle]]**  |
| FText | **[[TextBlockText]]**  |
| UWidget::FGetText | **[[TextBlockTextDelegate]]**  |
| bool | **[[bDoNotReverseHoveredStateUponMouseLeave]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200
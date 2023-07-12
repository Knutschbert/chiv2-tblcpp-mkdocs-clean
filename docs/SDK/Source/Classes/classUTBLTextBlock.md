---
title: UTBLTextBlock
type: class
aliases: UTBLTextBlock
share: false

---

# UTBLTextBlock





Inherits from URichTextBlock

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[SetColorAndOpacity]]**(FSlateColor InColorAndOpacity) |
| void | **[[SetFont]]**(FSlateFontInfo InFontInfo) |
| void | **[[SetFontSize]]**(int32 Size) |
| void | **[[SetShadowColorAndOpacity]]**(FLinearColor InShadowColorAndOpacity) |
| void | **[[SetShadowOffset]]**(FVector2D InShadowOffset) |
| void | **[[SetWrapTextAt]]**(float InWrapTextAt) |
| | **[[UTBLTextBlock]]**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| FString | **[[AttributeRegexPattern]]**  |
| FLinearColor | **[[Color]]**  |
| FSlateColor | **[[ColorAndOpacity]]**  |
| UWidget::FGetSlateColor | **[[ColorAndOpacityDelegate]]**  |
| UClass * | **[[DefaultEmbeddedKeyBindingClass]]**  |
| FString | **[[ElementRegexPattern]]**  |
| UDataTable * | **[[EmbeddedWidgetsTable]]**  |
| FSlateFontInfo | **[[Font]]**  |
| FGetKeybindingWidgetDelegate | **[[GetKeybindingWidgetDelegateEvent]]**  |
| FVector2D | **[[IconSize]]**  |
| TArray< [UWidgetDecorator](/docs/SDK/Source/Classes/classUWidgetDecorator.md) * > | **[[KeyBindingDecorators]]**  |
| TMap< FString, TSubclassOf< UUserWidget > > | **[[RunNameToWidgetClass]]**  |
| FLinearColor | **[[ShadowColorAndOpacity]]**  |
| UWidget::FGetLinearColor | **[[ShadowColorAndOpacityDelegate]]**  |
| FVector2D | **[[ShadowOffset]]**  |
| bool | **[[bOverrideDefaultTextStyle]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
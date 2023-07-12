---
title: USpinBoxInt
type: class
aliases: USpinBoxInt
share: false

---

# USpinBoxInt





Inherits from UWidget

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ClearMaxSliderValue]]**() |
| void | **[[ClearMaxValue]]**() |
| void | **[[ClearMinSliderValue]]**() |
| void | **[[ClearMinValue]]**() |
| | **[[DECLARE_DYNAMIC_MULTICAST_DELEGATE]]**(FOnSpinBoxBeginSliderMovement ) |
| | **[[DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam]]**(FOnSpinBoxValueChangedEvent , int32 , InValue ) |
| | **[[DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams]]**(FOnSpinBoxValueCommittedEvent , int32 , InValue , TEnumAsByte< ETextCommit::Type > , CommitMethod ) |
| int32 | **[[GetMaxSliderValue]]**() const |
| int32 | **[[GetMaxValue]]**() const |
| int32 | **[[GetMinSliderValue]]**() const |
| int32 | **[[GetMinValue]]**() const |
| int32 | **[[GetValue]]**() const |
| void | **[[SetForegroundColor]]**(FSlateColor InForegroundColor) |
| void | **[[SetMaxSliderValue]]**(int32 NewValue) |
| void | **[[SetMaxValue]]**(int32 NewValue) |
| void | **[[SetMinSliderValue]]**(int32 NewValue) |
| void | **[[SetMinValue]]**(int32 NewValue) |
| void | **[[SetValue]]**(int32 NewValue) |
| | **[[USpinBoxInt]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[[ClearKeyboardFocusOnCommit]]**  |
| int32 | **[[Delta]]**  |
| FSlateFontInfo | **[[Font]]**  |
| FSlateColor | **[[ForegroundColor]]**  |
| int32 | **[[MinDesiredWidth]]**  |
| FOnSpinBoxBeginSliderMovement | **[[OnBeginSliderMovement]]**  |
| FOnSpinBoxValueChangedEvent | **[[OnEndSliderMovement]]**  |
| FOnSpinBoxValueChangedEvent | **[[OnValueChanged]]**  |
| FOnSpinBoxValueCommittedEvent | **[[OnValueCommitted]]**  |
| bool | **[[SelectAllTextOnCommit]]**  |
| int32 | **[[SliderExponent]]**  |
| USlateWidgetStyleAsset * | **[[Style]]**  |
| int32 | **[[Value]]**  |
| UWidget::FGetInt32 | **[[ValueDelegate]]**  |
| FSpinBoxStyle | **[[WidgetStyle]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| int32 | **[[MaxSliderValue]]**  |
| int32 | **[[MaxValue]]**  |
| int32 | **[[MinSliderValue]]**  |
| int32 | **[[MinValue]]**  |
| uint8 | **[[bOverride_MaxSliderValue]]**  |
| uint8 | **[[bOverride_MaxValue]]**  |
| uint8 | **[[bOverride_MinSliderValue]]**  |
| uint8 | **[[bOverride_MinValue]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
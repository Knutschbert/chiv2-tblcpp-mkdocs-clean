---
title: UTBLUserWidget
type: class
aliases: UTBLUserWidget
share: false

---

# UTBLUserWidget





Inherits from UUserWidget

Inherited by [UHUDContainerWidget](/docs/SDK/Source/Classes/classUHUDContainerWidget.md), [UPartyList](/docs/SDK/Source/Classes/classUPartyList.md), [UPartyListEntry](/docs/SDK/Source/Classes/classUPartyListEntry.md), [UTBLGameUpdateContentWidget](/docs/SDK/Source/Classes/classUTBLGameUpdateContentWidget.md), [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md), [UTBLScreenWidget](/docs/SDK/Source/Classes/classUTBLScreenWidget.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md) * | **[[GetScreenManager]]**() const |
| void | **[[HandleGamepadNavigationModeChanged]]**(EGamepadNavigationMode Mode) |
| bool | **[[IsWidgetDisabled]]**() const |
| void | **[[IsWidgetEnabled]]**(EWidgetDisableType & Result) |
| void | **[[K2_Highlight]]**() |
| void | **[[K2_OnFocusChanging]]**() |
| void | **[[K2_Unhighlight]]**() |
| void | **[[NativeHighlight]]**() |
| void | **[[NativeUnhighlight]]**() |
| void | **[[PlayAdvancedAnimation]]**(const UWidgetAnimation * InAnimation, const UCurveFloat * InterpolationCurve, float StartAtTime, float LoopBackToTime, float EndAtTime, bool bIsNormalizedCurve, float AnimationSpeed, int32 NumLoopsToPlay, bool bResumeFromLastTime, float Duration, float MaxDuration) |
| void | **[[PlayInterruptableAnimation]]**(UWidgetAnimation * InAnimation, float StartAtTime, int32 NumLoopsToPlay, FName InterruptGroup, bool bPlayInReverse, bool bReverseExisting) |
| | **[[UTBLUserWidget]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| [UTBLUserWidget](/docs/SDK/Source/Classes/classUTBLUserWidget.md) * | **[[GetRadioGroupSelection]]**(FName Group) |
| void | **[[SetSelfAsRadioGroupSelection]]**(FName Group) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [UTBLUMGSequencePlayer](/docs/SDK/Source/Classes/classUTBLUMGSequencePlayer.md) * > | **[[ActiveTBLSequencePlayers]]**  |
| TArray< [FButtonCallout](/docs/SDK/Source/Classes/structFButtonCallout.md) > | **[[ButtonCallouts]]**  |
| FOnNavigationPathEvent | **[[EventAddedToFocusPath]]**  |
| FOnNavigationPathEvent | **[[EventRemovedFromFocusPath]]**  |
| TMap< FName, TWeakObjectPtr< UUMGSequencePlayer > > | **[[InterruptableSequencePlayers]]**  |
| bool | **[[IsWidgetDisabledInDemoMode]]**  |
| bool | **[[IsWidgetDisabledInShippingWIP]]**  |
| FOnHighlightEvent | **[[OnHighlight]]**  |
| FOnHighlightEvent | **[[OnUnhighlight]]**  |
| bool | **[[bIsHighlighted]]**  |
| bool | **[[bIsInFocusPath]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
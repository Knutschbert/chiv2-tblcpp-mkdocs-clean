---
title: UTBLScreenWidget
type: class
aliases: UTBLScreenWidget
share: false

---

# UTBLScreenWidget





Inherits from [UTBLUserWidget](/docs/SDK/Source/Classes/classUTBLUserWidget.md), UUserWidget

Inherited by [UTBLDialogWidget](/docs/SDK/Source/Classes/classUTBLDialogWidget.md), [UTBLKeymapWidget](/docs/SDK/Source/Classes/classUTBLKeymapWidget.md), [UTBLSocialScreen](/docs/SDK/Source/Classes/classUTBLSocialScreen.md), [UTBLStoreWidget](/docs/SDK/Source/Classes/classUTBLStoreWidget.md), [UTBLTitleScreen](/docs/SDK/Source/Classes/classUTBLTitleScreen.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AddButtonAction]]**(FName ButtonID, int32 ButtonIndex) |
| bool | **[[BlockKeyPress]]**(const EWeaponAbilitySlotKey WeaponAbilitySlotKey) const |
| void | **[[FireButtonAction]]**(FName ButtonID) |
| void | **[[FireDefaultButtonAction]]**(int32 ButtonIndex) |
| void | **[[FireUpdateNotifications]]**() |
| void | **[[OnClosedScreen]]**() |
| void | **[[OnOpenedScreen]]**() |
| void | **[[OnOutroAnimationDone]]**(bool bWasScreenClosed) |
| void | **[[OnPausedScreen]]**() |
| void | **[[OnResumedScreen]]**() |
| void | **[[PlayIntroAnimation]]**(UWidgetAnimation * InAnimation, float StartAtTime, int32 NumLoopsToPlay, bool bReverseExisting) |
| void | **[[PlayOutroAnimation]]**(UWidgetAnimation * InAnimation, float StartAtTime, int32 NumLoopsToPlay, bool bReverseExisting) |
| void | **[[PopOffParentStack]]**() |
| void | **[[PushScreenToParentStack]]**([UTBLScreenWidget](/docs/SDK/Source/Classes/classUTBLScreenWidget.md) * NextScreen) |
| void | **[[RequestPlayerInput]]**(bool WantsInput) |
| bool | **[[ShouldOverrideIsFocusable]]**() const |
| bool | **[[ShouldShowMouseCursorOnInputCapture]]**() const |
| | **[[UTBLScreenWidget]]**() |
| void | **[[UpdateNotifications]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[BP_OnBlockKeyPress]]**(const EWeaponAbilitySlotKey WeaponAbilitySlotKey) const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TWeakObjectPtr< UUMGSequencePlayer > | **[[OutroPlayer]]**  |
| [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md) * | **[[ParentScreenManager]]**  |
| FName | **[[StackName]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< EWeaponAbilitySlotKey > | **[[BlockedWeaponAbilitySlotKeys]]**  |
| EMouseLockMode | **[[MouseLockMode]]**  |
| ESlateVisibility | **[[NonTopmostVisibility]]**  |
| int32 | **[[PlayerInputIdAtInputModeChange]]**  |
| ESlateVisibility | **[[TopmostVisibilty]]**  |
| bool | **[[bHideCursorDuringCapture]]**  |
| bool | **[[bInputUIAndGame]]**  |
| bool | **[[bIsScreenClosed]]**  |
| bool | **[[bModifyVisibilityOnPushAndPop]]**  |
| bool | **[[bPopWhenEscapePressed]]**  |
| bool | **[[bTopmostScreen]]**  |
| bool | **[[bWantsInputFocusOnTopmost]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
---
title: UTBLScreenManager
type: class
aliases: UTBLScreenManager
share: false

---

# UTBLScreenManager





Inherits from [UTBLUserWidget](/docs/SDK/Source/Classes/classUTBLUserWidget.md), [ITBLKeymapWidgetInterface](/docs/SDK/Source/Classes/classITBLKeymapWidgetInterface.md), UUserWidget

Inherited by [UTBLDialogManager](/docs/SDK/Source/Classes/classUTBLDialogManager.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BP_FadeIn]]**(const float PlaybackSpeed) |
| void | **[[BP_FadeOut]]**(const float PlaybackSpeed) |
| void | **[[ClearScreenStack]]**(UOverlay * Overlay) |
| UWidget * | **[[GetActiveCrosshair]]**() |
| EGamepadInputMode | **[[GetGamepadInputMove]]**() |
| EGamepadNavigationMode | **[[GetGamepadNavigationMode]]**() |
| void | **[[GetTopScreen]]**(UOverlay * Overlay, FName & OutScreenName, [UTBLScreenWidget](/docs/SDK/Source/Classes/classUTBLScreenWidget.md) *& OutScreen) |
| void | **[[OpenDebugMenu]]**([UBlueprintDebugMenuComponent](/docs/SDK/Source/Classes/classUBlueprintDebugMenuComponent.md) * DebugMenuComponent) |
| void | **[[PopScreenStack]]**(UOverlay * Overlay) |
| void | **[[PopShowMouseCursorStack]]**(UObject * Object) |
| void | **[[PushNamedScreenToStack]]**([UTBLScreenWidget](/docs/SDK/Source/Classes/classUTBLScreenWidget.md) * Screen, UOverlay * Overlay, FName ScreenName) |
| void | **[[PushScreenToStack]]**([UTBLScreenWidget](/docs/SDK/Source/Classes/classUTBLScreenWidget.md) * Screen, UOverlay * Overlay) |
| void | **[[PushShowMouseCursorStack]]**(UObject * Object) |
| bool | **[[RemoveScreenFromStack]]**([UTBLScreenWidget](/docs/SDK/Source/Classes/classUTBLScreenWidget.md) * Screen, UOverlay * Overlay, bool bPopOnly, bool bDontTellScreen) |
| void | **[[SetActiveCrosshair]]**(UWidget * Crosshair) |
| void | **[[SetHudVisibility]]**(bool bVisible) |
| void | **[[SetWidgetAsRadioGroupSelection]]**(FName Group, [UTBLUserWidget](/docs/SDK/Source/Classes/classUTBLUserWidget.md) * InSelection) |
| void | **[[SwapNamedScreenToFront]]**(FName ScreenName, UOverlay * Overlay) |
| | **[[UTBLScreenManager]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FOnButtonCalloutsChanged | **[[OnButtonCalloutsChanged]]**  |
| FOnGamepadInputModeSwitchEvent | **[[OnGamepadInputModeChanged]]**  |
| FOnGamepadNavigationModeSwitchEvent | **[[OnGamepadNavigationModeChanged]]**  |
| FOnKeyBindChangedDelegate | **[[OnKeyBindChanged]]**  |
| FOnPreviewMouseButtonDownEventDelegate | **[[OnPreviewMouseButtonDownEvent]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| UWidget * | **[[ActiveCrosshair]]**  |
| TMap< FName, [UTBLUserWidget](/docs/SDK/Source/Classes/classUTBLUserWidget.md) * > | **[[RadioGroups]]**  |
| TArray< [FScreenStack](/docs/SDK/Source/Classes/structFScreenStack.md) > | **[[ScreenStacks]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
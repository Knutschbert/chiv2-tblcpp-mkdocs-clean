---
title: UUIBlueprintLibrary
type: class
aliases: UUIBlueprintLibrary
share: false

---

# UUIBlueprintLibrary





Inherits from UBlueprintFunctionLibrary

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [UHudMarkerDisplayComponent](/docs/SDK/Source/Classes/classUHudMarkerDisplayComponent.md) * | **[[AddHudMarkerComponentToActor]]**(AActor * Actor, EFaction VisibleToFaction, TSubclassOf< [UHudMarkerDisplayComponent](/docs/SDK/Source/Classes/classUHudMarkerDisplayComponent.md) > Class, bool bReplicates) |
| void | **[[AttemptThrottledOnKilledUIActions]]**(EFrameThrottleBranch & Branches) |
| FText | **[[ConvertTimespanToText]]**(FTimespan Timespan) |
| void | **[[FocusOnBestWidgetOrChild]]**(UWidget * Widget) |
| FInputActionKeyMapping | **[[GetActionBindingFromName]]**(FName ActionName, UObject * WorldContextObject) |
| [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md) * | **[[GetActiveScreenManager]]**(UObject * WorldContextObject) |
| [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md) * | **[[GetActiveScreenManagerImpure]]**(UObject * WorldContextObject) |
| void | **[[GetAllKeysFromActionBindingName]]**(const FString & ActionName, TArray< FKey > & NonGamePad, TArray< FKey > & Gamepad, UObject * WorldContextObject) |
| void | **[[GetAllMapNames]]**(TArray< FName > & OutAssetNames, const FString & MapPath) |
| TArray< [FButtonCallout](/docs/SDK/Source/Classes/structFButtonCallout.md) > | **[[GetButtonCallouts]]**(UWidget * Target) |
| FLinearColor | **[[GetFactionColor]]**(EFaction Faction, ETeamUIColorType ColorType) |
| FText | **[[GetFactionName]]**(EFaction Faction) |
| TArray< EFaction > | **[[GetFactionOrder]]**(EFaction A, EFaction B) |
| FKey | **[[GetGamepadAcceptButton]]**() |
| FKey | **[[GetGamepadBackButton]]**() |
| [FKeyDisplayInfo](/docs/SDK/Source/Classes/structFKeyDisplayInfo.md) | **[[GetKeyDisplayInfoFromTable]]**(FKey Key, UDataTable * Table) |
| FKey | **[[GetKeyFromActionBindingName]]**(const FString & ActionName, UObject * WorldContextObject) |
| FKey | **[[GetKeyFromAxisBindingName]]**(const FString & ActionName, UObject * WorldContextObject) |
| FKey | **[[GetKeyFromButtonCallout]]**([FButtonCallout](/docs/SDK/Source/Classes/structFButtonCallout.md) Callout, UWidget * WorldContextObject) |
| FText | **[[GetKeyTextFromActionBindingName]]**(const FString & ActionName, FInputActionKeyMapping & ActionMappingOut, bool bLongDisplayName, EGamepadInputMode InputMode, UObject * WorldContextObject) |
| EUINavigation | **[[GetNavigationDirectionFromAnalog]]**(const FAnalogInputEvent & InAnalogEvent, bool & bInvalid) |
| EUINavigation | **[[GetNavigationDirectionFromKey]]**(const FKeyEvent & InKeyEvent, bool & bInvalid) |
| [UTBLLocalPlayer](/docs/SDK/Source/Classes/classUTBLLocalPlayer.md) * | **[[GetOwningTBLLocalPlayer]]**(UObject * Target) |
| [ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * | **[[GetOwningTBLPlayerController]]**(UObject * Target) |
| bool | **[[IsHandled]]**(const FEventReply & EventReply) |
| FName | **[[Key_GetFName]]**(const FKey & Key) |
| FText | **[[Key_GetShortDisplayName]]**(const FKey & Key) |
| FLinearColor | **[[LinearColorFromHsluv]]**(float H, float S, float L) |
| void | **[[ListenForKeybindings]]**() |
| FLinearColor | **[[RandomLinearColorFromHsluv]]**(float h_min, float h_max, float s_min, float s_max, float l_min, float l_max) |
| void | **[[RegisterDisplayComponent]]**(const TScriptInterface< [IDisplayComponentInterface](/docs/SDK/Source/Classes/classIDisplayComponentInterface.md) > & DisplayComponent) |
| void | **[[ResetAllAnimations]]**(UUserWidget * Widget) |
| FEventReply | **[[RouteOnAnalogValueChanged]]**(UWidget * Widget, const FGeometry & MyGeometry, const FAnalogInputEvent & InAnalogInputEvent) |
| FEventReply | **[[RouteOnKeyCharToWidget]]**(UWidget * Widget, const FGeometry & MyGeometry, const FCharacterEvent & InCharEvent) |
| FEventReply | **[[RouteOnKeyDownToWidget]]**(UWidget * Widget, const FGeometry & MyGeometry, const FKeyEvent & InKeyEvent) |
| FEventReply | **[[RouteOnKeyUpToWidget]]**(UWidget * Widget, const FGeometry & MyGeometry, const FKeyEvent & InKeyEvent) |
| FEventReply | **[[RouteOnPreviewKeyDownToWidget]]**(UWidget * Widget, const FGeometry & MyGeometry, const FKeyEvent & InKeyEvent) |
| void | **[[SendGlobalGameNotification]]**(EGlobalGameNotificationCategory Category, FText Title, FText Body, FName Subcategory, UObject * Data, UObject * WorldContextObject) |
| void | **[[SetInputActionMode]]**(APlayerController * InPlayerController, EInputActionMode InInputActionMode) |
| bool | **[[ShouldDisableWorkInProgressFeatures]]**() |
| void | **[[StopListeningForKeybindings]]**() |
| | **[[UUIBlueprintLibrary]]**() |
| void | **[[UnregisterDisplayComponent]]**(const TScriptInterface< [IDisplayComponentInterface](/docs/SDK/Source/Classes/classIDisplayComponentInterface.md) > & DisplayComponent) |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200
---
title: UTBLGameInstance
type: class
aliases: UTBLGameInstance
share: false

---

# UTBLGameInstance





Inherits from UGameInstance

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[CanLeaveNativeSession]]**() |
| bool | **[[CanUseMatchmaker]]**() const |
| void | **[[ClearShowMouseCursorStackSuppressors]]**(const bool bUpdateMouseCursorImmediately) |
| FName | **[[GetCurrentState]]**() const |
| EGamepadInputMode | **[[GetLastGamepadInputMode]]**() const |
| int32 | **[[GetNativeSessionMemberCount]]**() |
| bool | **[[GetShowMouseCursor]]**() const |
| void | **[[GoToTutorialMap]]**() |
| void | **[[GrantFlavorEntitlement]]**(const FString & Entitlement) |
| bool | **[[IsCrossplayBlockedByOS]]**() |
| bool | **[[IsFirstLoadCompleted]]**() |
| bool | **[[IsInMainMenuMap]]**() const |
| bool | **[[IsMatchmakingQueueSelected]]**(const FName & QueueId) const |
| bool | **[[IsNativeSessionFull]]**() |
| bool | **[[IsNativeSessionHost]]**() |
| bool | **[[LastJoinFailed]]**() |
| void | **[[LeaveNativeSession]]**() |
| void | **[[OnPairingChangedNo]]**() |
| void | **[[OnPairingChangedYes]]**() |
| void | **[[OnPostMatchEndTimeChanged]]**(float Time) |
| void | **[[OnShowLoadingScreenPostMatch]]**() |
| void | **[[PollTitleDataAndNews]]**() |
| void | **[[PopShowMouseCursorStack]]**(UObject * Object) |
| void | **[[PopShowMouseCursorStackSuppressor]]**(UObject * Object) |
| void | **[[PushShowMouseCursorStack]]**(UObject * Object) |
| void | **[[PushShowMouseCursorStackSuppressor]]**(UObject * Object) |
| void | **[[ResetProfileData]]**() |
| void | **[[SetFirstLoadCompleted]]**(bool IsComplete) |
| void | **[[SetMatchmakingQueueSelected]]**(const FName & QueueId, bool IsSelected) |
| void | **[[ShowFreeWeekendUpsell]]**(int32 LocalUserNum) |
| void | **[[ShowPlatformSpecificPlayerDetails]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlayerState) |
| void | **[[TestNetworkDisconnect]]**() |
| | **[[UTBLGameInstance]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ClickedCancelConnect]]**() |
| void | **[[Disconnect]]**(UObject * WorldContextObject) |
| void | **[[ListLoadedStaticMeshWithNegativeScale]]**() |
| void | **[[PrintMorphTargetReport]]**() |
| void | **[[TestControllerDialog]]**() |
| void | **[[TestUserLoginDowngraded]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| uint8[15] | **[[AbbreviatedChatBlockedMessages]]**  |
| int32 | **[[AbbreviatedChatHistoryTrimThreshold]]**  |
| int32 | **[[AbbreviatedChatHistoryTrimToLength]]**  |
| int32[15] | **[[AbbreviatedChatMaxMessages]]**  |
| TSoftObjectPtr< UDataTable > | **[[AbilitiesDataTablePtr]]**  |
| TSoftObjectPtr< UDataTable > | **[[AbilitiesOverrideAssetDataTablePtr]]**  |
| TSoftObjectPtr< UDataTable > | **[[AbilitiesOverridesDataTablePtr]]**  |
| TSoftObjectPtr< [UAbilityConfig](/docs/SDK/Source/Classes/classUAbilityConfig.md) > | **[[AbilityConfigPtr]]**  |
| uint8[3] | **[[AllowedClosedCaptionTypes]]**  |
| [FAsyncGlobals](/docs/SDK/Source/Classes/structFAsyncGlobals.md) | **[[AsyncGlobals]]**  |
| TArray< UObject * > | **[[AsyncLoadedObjects]]**  |
| TMap< uint64, UTexture * > | **[[AvatarImages]]**  |
| FString | **[[CachedProfileDisplayName]]**  |
| uint8[15] | **[[ChatBlockedMessages]]**  |
| int32 | **[[ChatHistoryTrimThreshold]]**  |
| int32 | **[[ChatHistoryTrimToLength]]**  |
| [FCheckpoints](/docs/SDK/Source/Classes/structFCheckpoints.md) | **[[Checkpoints]]**  |
| float | **[[ClosedCaptionMaxDistanceSq]]**  |
| TArray< [FWwiseQuery](/docs/SDK/Source/Classes/structFWwiseQuery.md) > | **[[CompleteWwiseQueries]]**  |
| TSoftObjectPtr< UDataTable > | **[[CustomizationAnimationSetsDataTablePtr]]**  |
| TSoftObjectPtr< UAkAudioEvent > | **[[FallbackLoadingScreenMusicEvent]]**  |
| TSoftObjectPtr< UDataTable > | **[[GameUpdatesTablePtr]]**  |
| TSoftObjectPtr< UDataTable > | **[[KeyDisplayTablePtr]]**  |
| TArray< TSoftObjectPtr< UTexture > > | **[[KeyDisplayTextures]]**  |
| bool | **[[LightSabresLoaded]]**  |
| [UTBLLiveConfig](/docs/SDK/Source/Classes/classUTBLLiveConfig.md) * | **[[LiveConfig]]**  |
| FAssetLoaded | **[[OnCustomizationLoaded]]**  |
| FMatchmakingQueueStatisticsChanged | **[[OnMatchmakingQueueStatisticsChanged]]**  |
| FMotdUpdated | **[[OnMotdUpdated]]**  |
| FNativeSessionStatusChanged | **[[OnNativeSessionStatusChanged]]**  |
| FRefeshProfileDisplayName | **[[OnRefreshProfileDisplayName]]**  |
| FTitleDataUpdated | **[[OnTitleDataUpdated]]**  |
| FTitleNewsUpdated | **[[OnTitleNewsUpdated]]**  |
| FText | **[[PendingChatText]]**  |
| TWeakObjectPtr< UNetConnection > | **[[PendingLiveConfigConnection]]**  |
| FString | **[[PendingLiveConfigUrl]]**  |
| TArray< UAkAudioEvent * > | **[[PendingStoppedMusicEvents]]**  |
| TArray< [FWwiseQuery](/docs/SDK/Source/Classes/structFWwiseQuery.md) > | **[[PendingWwiseQueries]]**  |
| UAkAudioEvent * | **[[PlayingMusicEvent]]**  |
| int32 | **[[PlayingMusicEvent_PlayingID]]**  |
| [UTBLSaveProfileObject](/docs/SDK/Source/Classes/classUTBLSaveProfileObject.md) * | **[[ProfileSaveInstance]]**  |
| FString | **[[ReportBugURL]]**  |
| uint32 | **[[SavedBigNotificationCL]]**  |
| uint32 | **[[ShowBigNotificationOnCL]]**  |
| FStateChanged | **[[StateChanged]]**  |
| TSoftObjectPtr< UDataTable > | **[[WeaponAnimSetsPtr]]**  |
| bool | **[[bRegisteredWwiseCallback]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< TWeakObjectPtr< [UChatWidget](/docs/SDK/Source/Classes/classUChatWidget.md) > > | **[[ChatWidgets]]**  |
| TSoftClassPtr< [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md) > | **[[DemoMainMenuManagerClass]]**  |
| TSoftClassPtr< [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md) > | **[[DemoManagerClass]]**  |
| TSoftClassPtr< [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md) > | **[[DemoModeMainMenuManagerClass]]**  |
| [UTBLDialogManager](/docs/SDK/Source/Classes/classUTBLDialogManager.md) * | **[[DialogManager]]**  |
| TSoftClassPtr< [UTBLDialogManager](/docs/SDK/Source/Classes/classUTBLDialogManager.md) > | **[[DialogManagerClass]]**  |
| bool | **[[FirstLoadCompleted]]**  |
| UClass * | **[[LoadingScreenConfig]]**  |
| TSoftClassPtr< [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md) > | **[[MainMenuManagerClass]]**  |
| [UTBLMessageBus](/docs/SDK/Source/Classes/classUTBLMessageBus.md) * | **[[MessageBus]]**  |
| [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) | **[[PairingChangedDialogHandle]]**  |
| TSubclassOf< [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md) > | **[[PendingActiveScreenManager]]**  |
| FString | **[[PendingTravelDestination]]**  |
| TSoftClassPtr< [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md) > | **[[PlayingMenuManagerClass]]**  |
| TSoftClassPtr< [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md) > | **[[TitleScreenManagerClass]]**  |
| [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) | **[[TravelDialogHandle]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
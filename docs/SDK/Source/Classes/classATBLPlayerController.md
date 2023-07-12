---
title: ATBLPlayerController
type: class
aliases: ATBLPlayerController
share: false

---

# ATBLPlayerController





Inherits from APlayerController, IGameplayTaskOwnerInterface, [ITBLPlayerControllerInterface](/docs/SDK/Source/Classes/classITBLPlayerControllerInterface.md), [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

Inherited by [ATBLPlayerControllerCinematic](/docs/SDK/Source/Classes/classATBLPlayerControllerCinematic.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLPlayerController]]**() |
| void | **[[AddAllViewedItems]]**(TEnumAsByte< EAudioClassType::Type > CharacterType, EFaction Faction, FName AssetsTypeName) |
| void | **[[AddFriendById]]**(const FString & UniqueId) |
| void | **[[AddOnPossessedAutoVo]]**([FOnPossessedAutoVo](/docs/SDK/Source/Classes/structFOnPossessedAutoVo.md) OnPossessedAutoVo) |
| void | **[[AddUncheckedLevelUpResult]]**(const FPrimaryAssetId & NewLevelUpItem) |
| void | **[[AddViewedItem]]**(const FPrimaryAssetId & ItemId) |
| void | **[[Admin]]**(const FString & Cmd) |
| void | **[[AdminSay]]**(FString & Msg) |
| void | **[[AnalyticsQuery]]**(const FString & Map, const FString & BuildId) |
| bool | **[[AreCompoundActionKeysDown]]**(FName CompoundAction) |
| void | **[[AttachCameraToBone]]**(FName BoneName, bool bUseBoneRotation) |
| void | **[[AttachCameraToHorse]]**(FName BoneName, bool bUseBoneRotation) |
| void | **[[AttachCameraToProjectile]]**(bool bUseProjectileRotation) |
| void | **[[AttachCameraToWeapon]]**(FName WeaponName, bool bUseWeaponRotation) |
| void | **[[AutoInputRecord]]**() |
| void | **[[BroadcastDebugMessage]]**(const FString & Message, FColor TextColor, float Duration, bool bToAll, bool bTeamOnly) |
| void | **[[BugAnimation]]**() |
| bool | **[[CanPlayerCallKickVote]]**(APlayerState * KickTarget) |
| [FOwnershipResponse](/docs/SDK/Source/Classes/structFOwnershipResponse.md) | **[[CanUseCharacter]]**(const TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > & CharacterSubclass) |
| [FOwnershipResponse](/docs/SDK/Source/Classes/structFOwnershipResponse.md) | **[[CanUseLoadout]]**(const TSubclassOf< [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) > & LoadoutSelection) |
| [FOwnershipResponse](/docs/SDK/Source/Classes/structFOwnershipResponse.md) | **[[CanUseLoadoutItem]]**(const TSubclassOf< [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) > & LoadoutSelection, const TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > & Item) |
| void | **[[ChatMutePlayer]]**(APlayerState * Muted) |
| void | **[[ChatUnmutePlayer]]**(APlayerState * Unmuted) |
| bool | **[[CheckPersonalityOwnership]]**(TEnumAsByte< EAudioPersonalityType::Type > InPersonality, TEnumAsByte< EAudioClassType::Type > CharacterType, EFaction InFaction) |
| void | **[[CinematicSpectatorCamera]]**() |
| void | **[[ClearFlavorStats]]**() |
| void | **[[ClearLoadedSoundBanks]]**() |
| void | **[[ClearMovementMetrics]]**() |
| void | **[[ClearPlayerHasAcceptedNDA]]**() |
| void | **[[ClearSeenGameUpdates]]**() |
| void | **[[ClientAckDoneTravelling]]**() |
| void | **[[ClientAcknowledgeTeamRequest]]**(bool bSuccess, EFaction Faction) |
| void | **[[ClientCausedFallDeath]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) FallDamage) |
| void | **[[ClientClearPostMatchInfo]]**() |
| void | **[[ClientConfirmExit]]**() |
| void | **[[ClientDrawDebugTracerBox]]**(FVector Center, FVector Extent, FQuat Rotation, FColor Color) |
| void | **[[ClientDrawDebugTracerSphere]]**(FVector Center, float Radius, int32 Segments, FColor Color) |
| void | **[[ClientEndOnlineGame]]**() |
| void | **[[ClientFadeIn]]**(const float PlaybackSpeed) |
| void | **[[ClientFadeOut]]**(const float PlaybackSpeed) |
| void | **[[ClientGoingToSpawnAtSpawner]]**([ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * InSpawner) |
| void | **[[ClientHandleGlobalGameNotification]]**(EGlobalGameNotificationCategory Category, const FText & Title, const FText & Body, FName Subcategory, UObject * Data) |
| void | **[[ClientKicked]]**(const FText & KickReason) |
| void | **[[ClientNotifyForwardSpawnAwaitingCombatTimer]]**([AForwardSpawnWave](/docs/SDK/Source/Classes/classAForwardSpawnWave.md) * ForwardWave) |
| void | **[[ClientNotifyPendingSpawn]]**([ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * PendingSpawner, float ServerSpawnTimeSeconds) |
| void | **[[ClientNotifyWaveJoinResponse]]**([ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * Wave, bool bJoinedWaveSuccess) |
| void | **[[ClientOnBlockedAttack]]**(const EDefenderBlockedPolicy BlockPolicy, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter, const bool bWasProjectile) |
| void | **[[ClientOnCounteredAttack]]**(const EDefenderBlockedPolicy BlockPolicy, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter) |
| void | **[[ClientOnPlayerRevived]]**(APawn * RevivingPawn) |
| void | **[[ClientOnRevivedOtherPlayer]]**(APawn * RevivedPawn) |
| void | **[[ClientPlayEmote]]**(FName EmoteName) |
| void | **[[ClientPostAKSoundAtLocation]]**(FVector_NetQuantize Location, UAkAudioEvent * Sound) |
| void | **[[ClientPostAKSoundOnActor]]**(AActor * SoundActor, UAkAudioEvent * Sound) |
| void | **[[ClientPostAKSoundsOnActor]]**(AActor * SoundActor, const TArray< UAkAudioEvent * > & Sounds) |
| void | **[[ClientPostAkSound]]**(UAkAudioEvent * Sound) |
| void | **[[ClientPostGameMigrateToNewMatchmakingServer]]**(const FString & ConnectString) |
| void | **[[ClientPostGameStartMatchmaking]]**(bool bAlways) |
| void | **[[ClientPrintCustomizationItems]]**(const TArray< FPrimaryAssetId > & Items) |
| void | **[[ClientPushCmd]]**(const FString & Cmd) |
| void | **[[ClientReceiveChat]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * SenderPlayerState, const FString & S, EChatType::Type Type, bool IsSenderDev, FColor OverrideColor) |
| void | **[[ClientReceiveDeathRecap]]**([FDeathRecap](/docs/SDK/Source/Classes/structFDeathRecap.md) DeathRecap) |
| void | **[[ClientReceiveDecapHead]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * InDecapHead) |
| void | **[[ClientReceiveGameModeMessage]]**(const [FGameModeMessage](/docs/SDK/Source/Classes/structFGameModeMessage.md) & GameModeMessage) |
| void | **[[ClientReceiveGameModeMessages]]**(const TArray< [FGameModeMessage](/docs/SDK/Source/Classes/structFGameModeMessage.md) > & GameModeMessages) |
| void | **[[ClientReceiveLocalizedChat]]**(const FText & FormatText, EChatType::Type Type) |
| void | **[[ClientReceiveLocalizedObjectiveMessage]]**(const [FObjectiveMessage](/docs/SDK/Source/Classes/structFObjectiveMessage.md) & ObjectiveMessage) |
| void | **[[ClientReceiveObjectiveContextMessage]]**(const [FObjectiveContextMessage](/docs/SDK/Source/Classes/structFObjectiveContextMessage.md) ObjectiveContextMessage) |
| void | **[[ClientReceivedAutoBalanceNotification]]**(EFaction NewFaction) |
| void | **[[ClientRequestPostMatchInfo]]**() |
| void | **[[ClientSetSpectatorLocation]]**(FVector InLocation, FRotator InRotation) |
| void | **[[ClientSetVisibilityOfAllObjectiveZones]]**(bool IsVisible) |
| void | **[[ClientShowHudMarkerPointEvent]]**(FName HudMarkerTag, float TicketsModified, int32 TeamIndex) |
| void | **[[ClientShowLoadoutScreen]]**() |
| void | **[[ClientShowTeamSelectScreen]]**() |
| void | **[[ClientSpawnerStartAllowingControl]]**([ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * InSpawner, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char) |
| void | **[[ClientStartOnlineGame]]**() |
| void | **[[ClientSwitchToSpectator]]**() |
| void | **[[ClientUpdateVoiceStateForPlayer]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * NewPlayer) |
| void | **[[CloseMovementDebugger]]**() |
| void | **[[ClosePropertyDebugger]]**() |
| void | **[[CreateInputReplayComponent]]**() |
| void | **[[DebugSetPartySetting]]**(const FString & Key, const FString & Value) |
| void | **[[DestroyInputReplayComponent]]**() |
| void | **[[DevMode]]**(bool bActivate) |
| void | **[[DisableCameraOffset]]**() |
| void | **[[DumpFriendList]]**() |
| void | **[[DumpMovementMetrics]]**() |
| void | **[[DumpOwnership]]**() |
| void | **[[DumpStatsExec]]**(int32 Threshold) |
| void | **[[EchoPlayFabId]]**() |
| void | **[[ForceImmediateRespawn]]**() |
| void | **[[ForceSelfAutobalance]]**() |
| void | **[[GenerateStoreJSON]]**() |
| [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md) * | **[[GetActiveScreenManager]]**() |
| TArray< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > > | **[[GetAllowedCharacterClasses]]**() |
| TSubclassOf< [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) > | **[[GetAllowedLoadoutSelection]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > RequestedSubclass) |
| UAkComponent * | **[[GetAudioComponent]]**() |
| [UCampaignList](/docs/SDK/Source/Classes/classUCampaignList.md) * | **[[GetCampaignList]]**() const |
| [UTBLCampaignsCachedData](/docs/SDK/Source/Classes/classUTBLCampaignsCachedData.md) * | **[[GetCampaignsCachedData]]**() |
| void | **[[GetCatalogExec]]**(bool LevelAccessible, int32 LevelsAbove) |
| FPrimaryAssetId | **[[GetEquippedCustomizationWeaponAsset]]**(EWeaponTag WeaponTag, EFaction Faction, TEnumAsByte< EAudioClassType::Type > CharacterType) |
| void | **[[GetInputAnalogStickStateRaw]]**(TEnumAsByte< EControllerAnalogStick::Type > WhichStick, float & StickX, float & StickY) const |
| bool | **[[GetIsProfileDataLoaded]]**() |
| int32 | **[[GetLevel]]**(EOnlineStat Stat) |
| int32 | **[[GetLevelExec]]**(const FString & Stat) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| [ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * | **[[GetNextSpawnWave]]**() |
| int32 | **[[GetOnlineCommodity]]**(const FString & Key) |
| TArray< [FCustomizationEntry](/docs/SDK/Source/Classes/structFCustomizationEntry.md) > | **[[GetOwnerCustomizationItems]]**(TEnumAsByte< EAudioClassType::Type > CharacterType, EFaction Faction, FName AssetsTypeName, bool bPresetCompatible, bool bSort) |
| TArray< [FCustomizationEntry](/docs/SDK/Source/Classes/structFCustomizationEntry.md) > | **[[GetOwnerCustomizationWeaponItems]]**(EWeaponTag WeaponTag, EFaction Faction) |
| [FOwnershipResponse](/docs/SDK/Source/Classes/structFOwnershipResponse.md) | **[[GetOwnership]]**(const FPrimaryAssetId & AssetIdToCheck, bool BaseOnly) |
| [UQuestPool](/docs/SDK/Source/Classes/classUQuestPool.md) * | **[[GetQuestPool]]**() |
| [UTBLQuestsCachedData](/docs/SDK/Source/Classes/classUTBLQuestsCachedData.md) * | **[[GetQuestsCachedData]]**() |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[GetRandomUnlockedLoadoutItemForSlot]]**([ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) * LoadoutSelection, EInventoryItemSlot Slot) |
| bool | **[[GetRespawnTime]]**(float & TimeRemaining) |
| TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[GetSavedCharacterSubclass]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > ParentClass) |
| void | **[[GetSavedLoadout]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > RequestedSubclass, [FLoadout](/docs/SDK/Source/Classes/structFLoadout.md) & Loadout) |
| FTransform | **[[GetSpectatorPawnSpawnTransform]]**() |
| int32 | **[[GetStat]]**(EOnlineStat Stat) |
| int32 | **[[GetStatExec]]**(const FString & StatName) |
| float | **[[GetStatFloat]]**(const FString & StatName) |
| float | **[[GetStatFloatExec]]**(const FString & StatName) |
| [UTBLPlayerInput](/docs/SDK/Source/Classes/classUTBLPlayerInput.md) * | **[[GetTBLPlayerInput]]**() |
| float | **[[GetTeamDamage]]**() |
| float | **[[GetTimeUntilRespawn]]**() |
| void | **[[GetTimesKilledKilledByPlayer]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * OtherPlayer, int32 & OutTimesKilled, int32 & OutTimesKilledBy) |
| float | **[[GetToggleCameraGamepadInputHoldTimeThreshold]]**() const |
| int32 | **[[GetTotalTimesKilled]]**() |
| TArray< FPrimaryAssetId > | **[[GetUnlockedItemsBySubclass]]**(const TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > & CharacterSubclass) |
| TMap< FPrimaryAssetId, bool > | **[[GetUnlocksAtLevel]]**(int32 Level, EOnlineStat Stat) |
| void | **[[GiveWeapon]]**(FName WeaponName) |
| void | **[[GrantCurrencyExec]]**(const FString & Currency, int32 Amount) |
| void | **[[GrantFlavorEntitlementExec]]**(const FString & Entitlement) |
| void | **[[InputPlay]]**(FName ReplayName) |
| void | **[[InputRec]]**(FName ReplayName) |
| void | **[[InputStop]]**() |
| bool | **[[IsActionKeyDown]]**(FName ActionName) |
| FPrimaryAssetId | **[[IsCharacterRecentlyUnlocked]]**(const TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > & CharacterSubclass) |
| bool | **[[IsGhostCameraMode]]**() const |
| bool | **[[IsHeadlessClient]]**() |
| bool | **[[IsLoadoutEqualToSavedLoadout]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > RequestedSubclass, [FLoadout](/docs/SDK/Source/Classes/structFLoadout.md) Loadout) |
| FPrimaryAssetId | **[[IsLoadoutItemRecentlyUnlocked]]**(const TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > & CharacterSubclass, const TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > & Item) |
| bool | **[[IsPlayerChatMuted]]**(APlayerState * MutedPlayer) |
| void | **[[IsPlayerStateMuted]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * InPlayerState, bool & OutIsMuted) |
| bool | **[[IsPlayingCinematics]]**() |
| bool | **[[IsStatsLoaded]]**() |
| bool | **[[IsUsingGamepad]]**() |
| bool | **[[IsVOBankLoaded]]**(TEnumAsByte< EAudioPersonalityType::Type > PersonalityType) |
| bool | **[[IsViewedItem]]**(const FPrimaryAssetId & ItemId) |
| bool | **[[IsViewportFocused]]**() |
| void | **[[ListPlayers]]**() |
| void | **[[ListViewedItems]]**() const |
| void | **[[LoadBank]]**(const FString & BankName) |
| void | **[[LoadVOASync]]**(TEnumAsByte< EAudioPersonalityType::Type > PersonalityType) |
| void | **[[MovementDebugger]]**() |
| void | **[[MovementDebuggerLoadFile]]**(FName Filename) |
| void | **[[MuteClient]]**(bool Enabled) |
| void | **[[NotifyCausedDamage]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & Event) |
| void | **[[NotifyEnteredLeftLoadoutVolume]]**(UObject * LoadoutVolume, bool bInLoadoutVolume) |
| void | **[[OnAbilityInitiated]]**([AAbilityInvocation](/docs/SDK/Source/Classes/classAAbilityInvocation.md) * Invocation) |
| void | **[[OnEnumerateCloudFilesComplete]]**(const FPlatformInterfaceDelegateResult & Result) |
| void | **[[OnInputExitDeathCam]]**() |
| void | **[[OnLoadoutScreenState]]**(bool DidOpen) |
| void | **[[OnMatchMakingChanged]]**(bool bIsMatchmaking) |
| void | **[[OnReadUserFileComplete]]**(const FPlatformInterfaceDelegateResult & Result) |
| void | **[[OnRep_CheatsEnabled]]**() |
| void | **[[OnRep_bAutomaticallyChooseSpawnWave]]**() |
| void | **[[PS4TouchpadPressed]]**() |
| void | **[[PartySay]]**(FString & Msg) |
| void | **[[PendingSpawnExpired]]**([ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * PendingSpawner) |
| void | **[[PlayCameraShake]]**(FName CameraShakeName, bool bLoop) |
| void | **[[PlayDelayedCrossbowHapticsForPS5]]**() |
| int32 | **[[PlayGlobalVOEmote]]**([UCTBase](/docs/SDK/Source/Classes/classUCTBase.md) * CTPersonality, FName EmoteName, EFaction Faction, TEnumAsByte< EAudioClassType::Type > Class, EVOType VoType) |
| void | **[[PlayerCallKickVote]]**(APlayerState * KickTarget) |
| void | **[[PlayerIsBeingKicked]]**() |
| void | **[[PlayerPostGameFeedback]]**(int32 StarRating) |
| void | **[[PlayerSubmitVote]]**([UVotingInstance](/docs/SDK/Source/Classes/classUVotingInstance.md) * VotingInstance, FName Vote) |
| bool | **[[PlayerViewUnlockedLoadoutItem]]**(const TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > & CharacterSubclass, const TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > & Item) |
| bool | **[[PlayerViewedUnlockedSubclass]]**(const TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > & CharacterSubclass) |
| void | **[[PrepareBank]]**(const FString & BankName) |
| void | **[[PrepareEvent]]**(const FString & EventName) |
| void | **[[PressedMenuButton]]**() |
| void | **[[PrintCameraProperties]]**() |
| void | **[[PrintCameraShakeProperties]]**(FName CameraShakeName) |
| void | **[[PrintWeaponActionEvents]]**() |
| void | **[[PropertyDebugger]]**() |
| void | **[[PropertyDebuggerAdd]]**(const FString & PropertyName) |
| void | **[[PurchaseItem]]**(const FPrimaryAssetId & ItemId, const FString & Currency) |
| void | **[[PurchaseItemByString]]**(const FString & ItemId, const FString & Currency) |
| void | **[[PurchaseItemExec]]**(const FString & ItemId, const FString & Currency) |
| void | **[[PurchaseOffer]]**(const [FStoreOfferItem](/docs/SDK/Source/Classes/structFStoreOfferItem.md) & Offer) |
| void | **[[ReadFriendList]]**() |
| void | **[[RefreshRegionPingExec]]**() |
| void | **[[ReleasedMenuButton]]**() |
| void | **[[RemoveAllViewedItems]]**() |
| void | **[[RemoveCurrencyExec]]**(const FString & Currency, int32 Amount) |
| void | **[[RemoveFriendById]]**(const FString & UniqueId) |
| void | **[[RemoveLoadingScreenPanel]]**() |
| void | **[[RemoveViewedItem]]**(const FPrimaryAssetId & ItemId) |
| void | **[[ReportPlayer]]**(APlayerState * ReportedPlayer, const EPlayerReportCategory ReportCategory, const FString & ReportDescription) |
| void | **[[RequestJoinSpawnWave]]**([ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * Wave, bool bFromAutoSpawn) |
| void | **[[RequestLeaveSpawnWave]]**([ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * Wave) |
| void | **[[RequestRejectSpawnWave]]**([ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * Wave) |
| void | **[[RequestSwitchTeam]]**(EFaction RequestedFaction) |
| void | **[[ResetNativeAchievements]]**() |
| void | **[[SaveAutoInputRecord]]**() |
| void | **[[SaveCloudFilesIfDirty]]**() |
| void | **[[SaveLoadout]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > RequestedSubclass, TSubclassOf< [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) > LoadoutSelection, [FLoadout](/docs/SDK/Source/Classes/structFLoadout.md) RequestedLoadout) |
| void | **[[Say]]**(FString & Msg) |
| void | **[[SayChatType]]**(const FString & Msg, TEnumAsByte< EChatType::Type > ChatType, FColor OverrideColor) |
| void | **[[SendCancelPlayerMessageRequest]]**(int32 MessageId) |
| void | **[[SendPromptPlayerMessageReply]]**(int32 MessageId, bool Response) |
| void | **[[SendPromptPlayerMessageRequest]]**(FGameplayTag MessageTag, int32 & SentMessageId) |
| void | **[[ServerBPCheat]]**(const FString & CheatAndParams) |
| void | **[[ServerBroadcast]]**(const FString & Msg, EChatType::Type ChatType, FColor OverrideColor) |
| void | **[[ServerCheat]]**(FName CheatCommand, FName Param) |
| void | **[[ServerCheatObj]]**(FName CheatCommand, UObject * Param) |
| void | **[[ServerClearPS5MatchId]]**() |
| void | **[[ServerCloseMovementDebugger]]**() |
| void | **[[ServerClosePropertyDebugger]]**() |
| void | **[[ServerCommendPlayer]]**() |
| void | **[[ServerForceImmediateSpawn]]**() |
| void | **[[ServerForceSelfAutobalance]]**() |
| void | **[[ServerForgivePlayer]]**() |
| void | **[[ServerJoinSpawnWave]]**([ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * Wave, bool bFromAutoSpawn) |
| void | **[[ServerLeaveSpawnWave]]**([ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * Wave) |
| void | **[[ServerMovementDebugger]]**() |
| void | **[[ServerMovementDebuggerLoadFile]]**(FName Filename) |
| void | **[[ServerNotifyDoneTravelling]]**() |
| void | **[[ServerOnLoadoutScreenState]]**(bool DidOpen) |
| void | **[[ServerPrintAllDefaultCustomizationItems]]**() |
| void | **[[ServerPropertyDebugger]]**() |
| void | **[[ServerRegisterAsHeadlessClient]]**() |
| void | **[[ServerRejectSpawnWave]]**([ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * Wave) |
| void | **[[ServerReliableSetPlayingPrologue]]**(bool bInPlayingPrologue) |
| void | **[[ServerReportPlayer]]**(APlayerState * ReportedPlayer, const EPlayerReportCategory ReportCategory, const FString & ReportDescription) |
| void | **[[ServerRequestAnalyticsStart]]**(const FString & DataName) |
| void | **[[ServerRequestAnalyticsStop]]**() |
| void | **[[ServerRequestExit]]**() |
| void | **[[ServerResetIdleTime]]**() |
| void | **[[ServerResetPartyId]]**() |
| void | **[[ServerSay]]**(FString & Msg) |
| void | **[[ServerSendEquippedPersonality]]**(EAudioPersonalityType::Type PersonalityType) |
| void | **[[ServerSendOfflineAnalyticsEvent]]**([FOfflineAnalyticsEvent](/docs/SDK/Source/Classes/structFOfflineAnalyticsEvent.md) LocalAnalyticsEvent) |
| void | **[[ServerSendPostMatchInfo]]**([FClientPostMatchInfo](/docs/SDK/Source/Classes/structFClientPostMatchInfo.md) PostMatchInfo, const TArray< [FPerMinuteBucket](/docs/SDK/Source/Classes/structFPerMinuteBucket.md) > & PerMinuteBuckets) |
| void | **[[ServerSetHardwarePlatform]]**(EHardwarePlatform Platform) |
| void | **[[ServerSetPS5MatchId]]**(const FString & NewPS5MatchId) |
| void | **[[ServerSetPartyId]]**(const FString & PartyId) |
| void | **[[ServerSetPlatformOSSUniqueId]]**(const FUniqueNetIdRepl & UniqueIdRepl) |
| void | **[[ServerSetPlayerCustomization]]**(const TArray< [FCustomizationMap](/docs/SDK/Source/Classes/structFCustomizationMap.md) > & PlayerCustomization, [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PS) |
| void | **[[ServerSetSpectatorCamera]]**() |
| void | **[[ServerShowDebugCapture]]**(bool bActive, FName Category) |
| void | **[[ServerSpawnGoreHead]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * InPlayerState, uint8 DeadCharacterId, const FVector_NetQuantize & Location, const FVector_NetQuantize & Rotation, const FVector_NetQuantize & Impulse) |
| void | **[[ServerSubmitPlayerPostGameFeedback]]**(int32 StarRating) |
| void | **[[ServerSubmitVote]]**([UVotingInstance](/docs/SDK/Source/Classes/classUVotingInstance.md) * VotingInstance, FName Vote) |
| void | **[[ServerTBSActivateDevMode]]**(bool bActivate) |
| void | **[[ServerToggleAutospawn]]**(bool bEnabled, bool bLeaveCurrentWave) |
| void | **[[SetAllRegionPingExec]]**(int32 Ping) |
| void | **[[SetAltAttackWithMovement]]**(bool bEnable) |
| void | **[[SetAutoSprint]]**(bool bEnable) |
| void | **[[SetCameraOffset]]**(float X, float Y, float Z) |
| void | **[[SetCameraProperty]]**(FName PropertyName, const FString & Value) |
| void | **[[SetCameraRotation]]**(float Pitch, float Yaw, float Roll) |
| void | **[[SetCameraShakeProperty]]**(FName CameraShakeName, FName PropertyName, const FString & Value) |
| void | **[[SetHudVisibility]]**(bool bVisible) |
| void | **[[SetLastReadDeveloperMessageTime]]**(FDateTime ReadDeveloperMessageTime) |
| void | **[[SetListenerEnabled]]**(bool Enabled) |
| void | **[[SetLoadout]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > RequestedSubclass, [FLoadout](/docs/SDK/Source/Classes/structFLoadout.md) RequestedLoadout) |
| void | **[[SetMinimumSpawnDelayOverride]]**(float InMinimumSpawnDelayOverride) |
| void | **[[SetNewCustomizationForCurrentPawn]]**(const TArray< [FSwatchSelection](/docs/SDK/Source/Classes/structFSwatchSelection.md) > & Swatches) |
| void | **[[SetNewCustomizationForPawn]]**(const TArray< [FSwatchSelection](/docs/SDK/Source/Classes/structFSwatchSelection.md) > & Swatches, APawn * Char, EFaction Faction) |
| void | **[[SetPlayerHasAcceptedNDA]]**() |
| void | **[[SetPlayerHasAcceptedPurchaseDisclaimer]]**() |
| void | **[[SetPlayerHasPlayedTutorial]]**() |
| void | **[[SetPlayingPrologue]]**(bool bInPlayingPrologue) |
| void | **[[SetRandomLoadout]]**([FLoadout](/docs/SDK/Source/Classes/structFLoadout.md) & Loadout) |
| void | **[[SetRegionPingExec]]**(const FString & Region, int32 Ping) |
| void | **[[SetShowPlayerListOnStartupInOverview]]**(bool bShow) |
| void | **[[SetSpectatorCamera]]**() |
| void | **[[SetStat]]**(const FString & StatName, int32 StatValue) |
| void | **[[SetStatFloat]]**(const FString & StatName, float StatValue) |
| void | **[[SetStatOriginal]]**(const FString & StatType, int32 StatValue) |
| void | **[[SetupCameraTargetOnDeath]]**(APawn * P, FName AttachSocketName) |
| bool | **[[ShouldClearDebugTracers]]**() const |
| bool | **[[ShouldDisplayNDA]]**() |
| bool | **[[ShouldDisplaySwingThroughInfo]]**() const |
| bool | **[[ShouldDrawBackSwingCheck]]**() const |
| bool | **[[ShouldDrawCamera]]**() const |
| bool | **[[ShouldDrawClientDebugTracers]]**() const |
| bool | **[[ShouldDrawDebugHorseImpact]]**() const |
| bool | **[[ShouldDrawDebugMeleeHit]]**() const |
| bool | **[[ShouldDrawDebugParryHit]]**() const |
| bool | **[[ShouldDrawDebugProjectile]]**() const |
| bool | **[[ShouldDrawDebugRangedInaccuracy]]**() const |
| bool | **[[ShouldDrawDebugShield]]**() const |
| bool | **[[ShouldDrawDebugTracerCache]]**() const |
| bool | **[[ShouldDrawDebugTracerDirection]]**() const |
| bool | **[[ShouldDrawDebugTracers]]**() const |
| bool | **[[ShouldDrawDebugWeaponTip]]**() const |
| bool | **[[ShouldDrawFacingCheck]]**() const |
| bool | **[[ShouldDrawVisibilityCheck]]**() const |
| void | **[[ShowIngameMenu]]**() |
| void | **[[ShowMessageDialog]]**(FText Message) |
| void | **[[ShowMyParryBox]]**() |
| void | **[[ShowOtherParryBoxes]]**() |
| void | **[[ShuffleLoadout]]**(bool bShouldShuffle) |
| [UMovementDebugger](/docs/SDK/Source/Classes/classUMovementDebugger.md) * | **[[SpawnMovementDebugger]]**() |
| void | **[[SpawnWaveNoLongerJoinable]]**([ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * Wave) |
| void | **[[StartRangedWeaponWarning]]**(float DrawStrength, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * DrawnWeapon, FName AttackName) |
| void | **[[StopCameraShake]]**(FName CameraShakeName) |
| void | **[[Suicide]]**() |
| void | **[[SwitchToSpectator]]**() |
| void | **[[TBLClientSetControlRotation]]**(FRotator ClientRotation) |
| void | **[[TeamSay]]**(FString & Msg) |
| void | **[[ToggleAutospawn]]**(bool bEnabled, bool bLeaveCurrentWave) |
| void | **[[ToggleCamera]]**() |
| void | **[[ToggleFriendlyMarkers]]**() |
| void | **[[ToggleGhostCameraMode]]**() |
| void | **[[ToggleHud]]**() |
| void | **[[ToggleIgnoreAI]]**() |
| void | **[[UnPrepareAllVOEVents]]**() |
| void | **[[UnloadBank]]**(const FString & BankName) |
| void | **[[UpdateUncheckedItems]]**() |
| void | **[[UpdateVoiceStateForAllPlayers]]**() |
| void | **[[VOIPMuteLocalExec]]**(bool Mute) |
| void | **[[VOIPSetRemoteVolumeExec]]**(float Volume) |
| void | **[[VerifyCustomizationOnlineOwnership]]**(bool bOnOnlineStatsLoaded) |
| void | **[[VoteStarted]]**([UVotingInstance](/docs/SDK/Source/Classes/classUVotingInstance.md) * VotingInstance) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[CanSwitchCamera]]**() const |
| void | **[[ClearServerHistoryList]]**() |
| void | **[[ClientApprovedLoadout]]**(bool IsLoadoutApproved, TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > RequestedSubclass, [FLoadout](/docs/SDK/Source/Classes/structFLoadout.md) RequestedLoadout) |
| void | **[[ClientBroadcastDebugMessage]]**(const FString & Message, FColor TextColor, float Duration, bool bToAll, bool bTeamOnly) |
| void | **[[ClientCancelPlayerMessageRequest]]**(int32 MessageId) |
| void | **[[ClientNotifyCausedDamage]]**(const [FDamageTakenEventCompressed](/docs/SDK/Source/Classes/structFDamageTakenEventCompressed.md) Event) |
| void | **[[ClientPromptPlayerMessageRequest]]**(FGameplayTag MessageTag, int32 MessageId) |
| void | **[[DisplayDebugScrollDown]]**() |
| void | **[[DisplayDebugScrollReleased]]**() |
| void | **[[DisplayDebugScrollUp]]**() |
| void | **[[DisplaySwingThroughInfo]]**(bool bEnable) |
| void | **[[DrawAllTracers]]**(bool bEnable) |
| void | **[[DrawBackSwingCheck]]**(bool bEnable) |
| void | **[[DrawCamera]]**(bool bEnable) |
| void | **[[DrawClientTracers]]**(bool bEnable) |
| void | **[[DrawFacingCheck]]**(bool bEnable) |
| void | **[[DrawHorseImpact]]**(bool bEnable) |
| void | **[[DrawMeleeHit]]**(bool bEnable) |
| void | **[[DrawParryHit]]**(bool bEnable) |
| void | **[[DrawProjectile]]**(bool bEnable) |
| void | **[[DrawRangedInaccuracy]]**(bool bEnable) |
| void | **[[DrawShield]]**(bool bEnable) |
| void | **[[DrawSocket]]**(FName SocketName) |
| void | **[[DrawSpectatorCamera]]**(bool bEnable) |
| void | **[[DrawTracerCache]]**(bool bEnable) |
| void | **[[DrawTracerDirection]]**(bool bEnable) |
| void | **[[DrawTracers]]**(bool bEnable) |
| void | **[[DrawTracersClear]]**(bool bEnable) |
| void | **[[DrawVisibilityCheck]]**(bool bEnable) |
| void | **[[DrawWeaponTip]]**(bool bEnable) |
| bool | **[[IsSelfCamera]]**() const |
| void | **[[OwningTeamChanged]]**([ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * NewOwningTeam) |
| void | **[[PlaySound]]**(UAkAudioEvent * Sound) |
| void | **[[PlayerStateMissingOnClientStart]]**(APlayerState * NewPlayerState) |
| void | **[[PrintDebugMessage]]**(const FString & Message, FColor TextColor, float Duration) |
| void | **[[ResetSelfCamera]]**() |
| void | **[[ServerAdminCmd]]**(const FString & Cmd) |
| void | **[[ServerBroadcastDebugMessage]]**(const FString & Message, FColor TextColor, float Duration, bool bToAll, bool bTeamOnly) |
| void | **[[ServerDisplaySwingThroughInfo]]**(bool bEnable) |
| void | **[[ServerDrawAllTracers]]**(bool bEnable) |
| void | **[[ServerDrawBackSwingCheck]]**(bool bEnable) |
| void | **[[ServerDrawFacingCheck]]**(bool bEnable) |
| void | **[[ServerDrawHorseImpact]]**(bool bEnable) |
| void | **[[ServerDrawParryHit]]**(bool bEnable) |
| void | **[[ServerDrawProjectile]]**(bool bEnable) |
| void | **[[ServerDrawShield]]**(bool bEnable) |
| void | **[[ServerDrawSpectatorCamera]]**(bool bEnable) |
| void | **[[ServerDrawTracerDirection]]**(bool bEnable) |
| void | **[[ServerDrawTracers]]**(bool bEnable) |
| void | **[[ServerDrawVisibilityCheck]]**(bool bEnable) |
| void | **[[ServerDrawWeaponTip]]**(bool bEnable) |
| void | **[[ServerOverrideSwatchIndex]]**(EInventorySlot Slot, int32 SwatchOverrideIndex) |
| void | **[[ServerPromptPlayerMessageReply]]**(int32 MessageId, bool Response) |
| void | **[[ServerRequestNextSpawnTeam]]**(EFaction RequestedFaction, bool bImmediatelySwitch) |
| void | **[[ServerSendMatchProfile]]**(const FString & Nickname, const FString & MachineId, const FString & MachineName, const FString & OperatingSystemId, const FString & CommandLine, [FTBLQualityLevels](/docs/SDK/Source/Classes/structFTBLQualityLevels.md) ScalabilitySettings) |
| void | **[[ServerSetForFFAPlayer]]**() |
| void | **[[ServerSetInitialLoadouts]]**(const TArray< [FSavedLoadout](/docs/SDK/Source/Classes/structFSavedLoadout.md) > & Loadouts) |
| void | **[[ServerSetLoadout]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > RequestedSubclass, [FLoadout](/docs/SDK/Source/Classes/structFLoadout.md) RequestedLoadout) |
| void | **[[ServerStopAnalytics]]**() |
| void | **[[ServerSuicide]]**() |
| void | **[[ServerSwitchToSpectator]]**() |
| void | **[[StartAllSayChat]]**() |
| void | **[[StartLastChannelChat]]**() |
| void | **[[StartTeamSayChat]]**() |
| void | **[[StopAnalytics]]**() |
| void | **[[StopSoundAllSounds]]**(UAkAudioEvent * Sound) |
| void | **[[SwitchClass]]**(int32 RequestedClassIndex, int32 RequestedSubclassIndex) |
| void | **[[SwitchTeam]]**(int32 RequestedTeamIndex) |
| void | **[[SwitchToSelfCamera]]**() |
| void | **[[TeamAppliedToPlayer]]**([ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * Team) |
| void | **[[ToggleCameraKeyPressed]]**() |
| void | **[[ToggleCameraKeyReleased]]**() |
| void | **[[ToggleGhost]]**() |
| void | **[[UpdateSelfCamera]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< FString > | **[[ArmourTypeStrings]]**  |
| FAutoBalanceNotificationReceived | **[[AutoBalanceNotificationReceived]]**  |
| FOnRepAutomaticallyChooseSpawnWave | **[[AutomaticallyChooseSpawnWaveReplicated]]**  |
| float | **[[BotTeamDamageScale]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[CharacterSoundDummy]]**  |
| [UCinematicsComponent](/docs/SDK/Source/Classes/classUCinematicsComponent.md) * | **[[CinematicsComponent]]**  |
| [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * | **[[ClientSpawnerStartAllowingControl_PendingSpawner]]**  |
| TArray< FString > | **[[CombatStateStrings]]**  |
| [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * | **[[CurrentPendingSpawner]]**  |
| [FCameraTargetParams](/docs/SDK/Source/Classes/structFCameraTargetParams.md) | **[[DeathCameraTargetParams]]**  |
| [FDebugProjectileHit](/docs/SDK/Source/Classes/structFDebugProjectileHit.md) | **[[DebugFakeProjectileHit]]**  |
| [FDebugProjectileHit](/docs/SDK/Source/Classes/structFDebugProjectileHit.md) | **[[DebugProjectileHit]]**  |
| TArray< [FDebugReliableRPC](/docs/SDK/Source/Classes/structFDebugReliableRPC.md) > | **[[DebugReliableRPC]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[DecapHead]]**  |
| TSoftClassPtr< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[DefaultClassChoice]]**  |
| float | **[[DisplayDebugScrollY]]**  |
| FGameModeMessageReceived | **[[GameModeMessageReceived]]**  |
| UGameplayTasksComponent * | **[[GameplayTasksComponent]]**  |
| TArray< [FSoundSwitchEntry](/docs/SDK/Source/Classes/structFSoundSwitchEntry.md) > | **[[HighPriorityAKSwitches]]**  |
| [UInputReplayComponent](/docs/SDK/Source/Classes/classUInputReplayComponent.md) * | **[[InputReplayComponent]]**  |
| [UItemPreVisualizationInterfaceHelper](/docs/SDK/Source/Classes/classUItemPreVisualizationInterfaceHelper.md) * | **[[ItemPreVisualizationHelper]]**  |
| FRotator | **[[LastClientSetRotation]]**  |
| float | **[[LastPingTime]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[LastPossessedCharacter]]**  |
| FDateTime | **[[LastReadDeveloperMessageTime]]**  |
| float | **[[LastVFov]]**  |
| TArray< [FSavedLoadout](/docs/SDK/Source/Classes/structFSavedLoadout.md) > | **[[LoadoutPerClass]]**  |
| double | **[[LoginTime]]**  |
| TArray< [FSoundSwitchEntry](/docs/SDK/Source/Classes/structFSoundSwitchEntry.md) > | **[[LowPriorityAKSwitches]]**  |
| float | **[[MinimumSpawnDelayOverride]]**  |
| [FLoadout](/docs/SDK/Source/Classes/structFLoadout.md) | **[[NextSpawnLoadout]]**  |
| [ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * | **[[NextSpawnWave]]**  |
| FNextSpawnWave | **[[NextSpawnWaveReplicated]]**  |
| [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * | **[[NextSpawner]]**  |
| FAcknowledgeTeamRequestSignature | **[[OnAcknowledgedTeamRequest]]**  |
| FTakenBlockDamageSignature | **[[OnBlockDamageTaken]]**  |
| FBlockedAttackSignature | **[[OnBlockedAttack]]**  |
| FCausedDamageSignature | **[[OnCausedDamage]]**  |
| FOnClearPlayerMessageRequest | **[[OnClearPlayerMessageRequest]]**  |
| FPossessedPawnSignature | **[[OnClientPossessedPawn]]**  |
| FOnClientPreTravel | **[[OnClientPreTravel]]**  |
| FCounteredAttackSignature | **[[OnCounteredAttack]]**  |
| FOnPlayerCustomizationsLoaded | **[[OnCustomizationsLoaded]]**  |
| FDeathRecapReplicatedSignature | **[[OnDeathRecapReplicated]]**  |
| FOnEnteredLeftLoadoutVolumeSignature | **[[OnEnteredLeftLoadoutVolume]]**  |
| FGameViewportLostFocus | **[[OnGameViewportLostFocus]]**  |
| FGameViewportReceivedFocus | **[[OnGameViewportReceivedFocus]]**  |
| FSpawningAtSpawner | **[[OnGoingToSpawnAtSpawner]]**  |
| FGotKeybindKey | **[[OnGotKeybindingKey]]**  |
| FOnHealingAppliedToCharacter | **[[OnHealingAppliedToCharacter]]**  |
| FJoinableSpawnWavesUpdated | **[[OnJoinableSpawnWavesUpdated]]**  |
| FOnPlayerEnteredOutOfCombatArea | **[[OnLocalPlayerEnteredOutOfCombatArea]]**  |
| FOnPlayerExitedOutOfCombatArea | **[[OnLocalPlayerExitedOutOfCombatArea]]**  |
| FOnLookInputUpdatedSignature | **[[OnLookInputUpdated]]**  |
| FOnLookRateInputUpdatedSignature | **[[OnLookRateInputUpdated]]**  |
| FOnObjectiveZonesVisiblityChanged | **[[OnObjectiveZonesVisiblityChanged]]**  |
| FOnPlayerCausedFallDamage | **[[OnPlayerCausedFallDamage]]**  |
| FPlayerControllerPostProcessInputSignature | **[[OnPlayerControllerPostProcessInput]]**  |
| FOnPlayerKicked | **[[OnPlayerKicked]]**  |
| FOnPlayerRevived | **[[OnPlayerRevived]]**  |
| FSpectatorSwitchSignature | **[[OnPlayerSelectedSpectatorMode]]**  |
| FOnRepPlayerState | **[[OnPlayerStateReplicated]]**  |
| FOnPlayerUsedItem | **[[OnPlayerUsedItem]]**  |
| FPossessedPawnSignature | **[[OnPossessedPawn]]**  |
| FOnProcessPlayerInput | **[[OnProcessPlayerInput]]**  |
| FOnProfileDataLoaded | **[[OnProfileDataLoaded]]**  |
| FOnPromptPlayerMessageReply | **[[OnPromptPlayerMessageReply]]**  |
| FOnPromptPlayerMessageRequest | **[[OnPromptPlayerMessageRequest]]**  |
| FPurchaseItemCompleted | **[[OnPurchaseCompleted]]**  |
| FGlobalGameNotification | **[[OnReceivedGlobalGameNotification]]**  |
| FOnReceivedLocalMessage | **[[OnReceivedLocalMessage]]**  |
| FOnReceivedPendingSpawn | **[[OnReceivedPendingSpawn]]**  |
| FJoinWaveResponse | **[[OnReceivedSpawnWaveJoinResponse]]**  |
| FOnPlayerRevived | **[[OnRevivedOtherPlayer]]**  |
| FSavedClassUnavailable | **[[OnSavedClassUnavailable]]**  |
| FServerApprovedLoadoutSignature | **[[OnServerApprovedLoadout]]**  |
| FOnSpectatorPawnDestroyed | **[[OnSpectatorPawnDestroyed]]**  |
| FTakenDamageSignature | **[[OnTakenDamage]]**  |
| FOnToggleCamera | **[[OnToggleCamera]]**  |
| FOnToggleControlMap | **[[OnToggleControlMap]]**  |
| FOnVotingStartedSignature | **[[OnVotingStarted]]**  |
| FOnZoomDisabled | **[[OnZoomDisabled]]**  |
| FOnZoomEnabled | **[[OnZoomEnabled]]**  |
| TSoftObjectPtr< [UTBLPS5BlockingHaptics](/docs/SDK/Source/Classes/classUTBLPS5BlockingHaptics.md) > | **[[PS5BlockingHaptic]]**  |
| TSoftObjectPtr< [UTBLPS5DamageHaptics](/docs/SDK/Source/Classes/classUTBLPS5DamageHaptics.md) > | **[[PS5PlayerDamageTakenHaptic]]**  |
| TSoftObjectPtr< [UTBLPS5GeneralHaptics](/docs/SDK/Source/Classes/classUTBLPS5GeneralHaptics.md) > | **[[PS5PlayerGeneralHaptic]]**  |
| TSoftObjectPtr< [UTBLPS5RangedWeaponHaptics](/docs/SDK/Source/Classes/classUTBLPS5RangedWeaponHaptics.md) > | **[[PS5PlayerRangedWeaponHaptic]]**  |
| TSoftObjectPtr< [UTBLPS5SiegeEngineHaptics](/docs/SDK/Source/Classes/classUTBLPS5SiegeEngineHaptics.md) > | **[[PS5PlayerSiegeEngineHaptic]]**  |
| TArray< [FSoundSwitchEntry](/docs/SDK/Source/Classes/structFSoundSwitchEntry.md) > | **[[PlayerExertionAKSwitches]]**  |
| [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * | **[[PlayerToCommendOrForgive]]**  |
| FString | **[[PostMatchMatchmakingConnectString]]**  |
| [FReplicationPredictionState](/docs/SDK/Source/Classes/structFReplicationPredictionState.md) | **[[PredictionState]]**  |
| FNextSpawnWave | **[[RequestedToJoinSpawnWave]]**  |
| TSoftClassPtr< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[SavedClassChoice]]**  |
| float | **[[SavedFov]]**  |
| TArray< [FSavedSubclass](/docs/SDK/Source/Classes/structFSavedSubclass.md) > | **[[SavedSubclassChoice]]**  |
| UInputComponent * | **[[SelfCameraInputComponent]]**  |
| float | **[[TeamDamage2MinThreshold]]**  |
| float | **[[TeamDamage30SecThreshold]]**  |
| int8 | **[[TeamDamageWarningLevel]]**  |
| float | **[[TimeSinceRotationInputWasNonZero]]**  |
| TArray< FPrimaryAssetId > | **[[UncheckedLevelUpItems]]**  |
| FPrimaryAssetType | **[[VOBankAssetType]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[WaitingForSpawnGoreHead]]**  |
| TArray< FString > | **[[WeaponActionNameStrings]]**  |
| TArray< [FSoundSwitchEntry](/docs/SDK/Source/Classes/structFSoundSwitchEntry.md) > | **[[WeaponAkSwitches]]**  |
| TArray< FString > | **[[WeaponNameStrings]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[WeaponSoundDummy]]**  |
| bool | **[[bAccessAllItems]]**  |
| bool | **[[bAltAttackWithMovement]]**  |
| bool | **[[bAutoSprint]]**  |
| uint8 | **[[bAutomaticallyChooseSpawnWave]]**  |
| bool | **[[bAwaitingInitialRequestedPlayerClass]]**  |
| uint8 | **[[bCheatsEnabled]]**  |
| bool | **[[bDisableHUDPostProcess]]**  |
| bool | **[[bFirstTimeSpectating]]**  |
| bool | **[[bIdleWarned]]**  |
| bool | **[[bIsHeadlessClient]]**  |
| bool | **[[bIsLoadoutScreenOpen]]**  |
| bool | **[[bIsPostMatchMatchmaking]]**  |
| bool | **[[bIsReadyToPostMatchMatchmakingTravel]]**  |
| bool | **[[bIsShufflingLoadout]]**  |
| bool | **[[bIsSpeaking]]**  |
| bool | **[[bIsTravelling]]**  |
| bool | **[[bPlayerHasAcceptedNDA]]**  |
| bool | **[[bPlayerHasAcceptedPurchaseDisclaimer]]**  |
| bool | **[[bPlayerHasPlayedTutorial]]**  |
| bool | **[[bPlayerIsWaitingToEnterSpectatorMode]]**  |
| bool | **[[bPlayerOpenedTutorial]]**  |
| bool | **[[bPlayerSelectedSpectatorMode]]**  |
| bool | **[[bPlayingPrologue]]**  |
| bool | **[[bReceivedInitialLoadouts]]**  |
| bool | **[[bShowMyParryBox]]**  |
| bool | **[[bShowOtherParryBoxes]]**  |
| bool | **[[bShowPlayerListOnStartupInOverview]]**  |
| bool | **[[bShuffleLoadout]]**  |
| bool | **[[bStartedForceRespawn]]**  |
| bool | **[[bTBSDevMode]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TSubclassOf< UCineCameraComponent > | **[[CinematicSpectatorCameraClass]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[CustomizationCharacter]]**  |
| TArray< UAkComponent * > | **[[DebugAkComponents]]**  |
| TArray< [FDebugSpectatorCamera](/docs/SDK/Source/Classes/structFDebugSpectatorCamera.md) > | **[[DebugSpectatorCamera]]**  |
| int32 | **[[DisplayDebugScrollDir]]**  |
| FName | **[[DrawDebugSocketName]]**  |
| FRotator | **[[LastControlRotation]]**  |
| float | **[[LastInputTime]]**  |
| APawn * | **[[LastReplicatedPawn]]**  |
| [FMatchSessionComplete](/docs/SDK/Source/Classes/structFMatchSessionComplete.md) | **[[MatchSessionComplete]]**  |
| int32 | **[[NextSpawnTeam]]**  |
| [FSelfCameraProperties](/docs/SDK/Source/Classes/structFSelfCameraProperties.md) | **[[SelfCamera]]**  |
| int32 | **[[SpamCheckIndex]]**  |
| float | **[[SpamCheckPeriod]]**  |
| int32 | **[[SpamCheckPeriodMaxMessages]]**  |
| TArray< float > | **[[SpamCheckPreviousMessages]]**  |
| float | **[[SpamMuteDurationIncreasePerMute]]**  |
| float | **[[SpamMuteDurationMax]]**  |
| float | **[[SpamMuteDurationMin]]**  |
| float | **[[SpamMutedDuration]]**  |
| float | **[[SpamMutedTime]]**  |
| float | **[[ThirdPersonFOVCap]]**  |
| bool | **[[bDebugIgnoreAI]]**  |
| bool | **[[bDisplaySwingThroughInfo]]**  |
| bool | **[[bDrawClientDebugTracers]]**  |
| bool | **[[bDrawDebugBackSwingCheck]]**  |
| bool | **[[bDrawDebugCamera]]**  |
| bool | **[[bDrawDebugFacingCheck]]**  |
| bool | **[[bDrawDebugHorseImpact]]**  |
| bool | **[[bDrawDebugMeleeHit]]**  |
| bool | **[[bDrawDebugParryHit]]**  |
| bool | **[[bDrawDebugProjectile]]**  |
| bool | **[[bDrawDebugRangedInaccuracy]]**  |
| bool | **[[bDrawDebugShield]]**  |
| uint8 | **[[bDrawDebugSpectatorCamera]]**  |
| bool | **[[bDrawDebugTracerCache]]**  |
| bool | **[[bDrawDebugTracerDirection]]**  |
| bool | **[[bDrawDebugTracers]]**  |
| bool | **[[bDrawDebugTracersClear]]**  |
| bool | **[[bDrawDebugVisibilityCheck]]**  |
| bool | **[[bDrawDebugWeaponTip]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200
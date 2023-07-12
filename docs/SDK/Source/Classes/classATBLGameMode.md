---
title: ATBLGameMode
type: class
aliases: ATBLGameMode
share: false

---

# ATBLGameMode





Inherits from AGameMode

Inherited by [ATBLFrontendGameMode](/docs/SDK/Source/Classes/classATBLFrontendGameMode.md), [ATBLGameMode_NativeBase](/docs/SDK/Source/Classes/classATBLGameMode__NativeBase.md), [ATutorialGameMode](/docs/SDK/Source/Classes/classATutorialGameMode.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLGameMode]]**() |
| void | **[[ActuallyLeaveMap]]**() |
| void | **[[AddBots]]**(int32 InNumBots) |
| void | **[[AddBotsEx]]**(int32 InNumBots, int32 Team, int32 Class) |
| void | **[[AddDummyBots]]**(int32 InNumBots) |
| void | **[[AddNullBots]]**(int32 InNumBots) |
| void | **[[AddPlayerBots]]**(int32 InNumBots, TArray< FString > ExcludeCategories) |
| void | **[[AddPlayerBotsEx]]**(int32 InNumBots, int32 Team, int32 Class, const FString & WhiteListName, TArray< FString > ExcludeCategories) |
| void | **[[AddPlayerBotsTrailerDefault]]**(int32 InNumBots) |
| void | **[[AddPlayerBotsWhitelist]]**(int32 InNumBots, const FString & WhiteListName) |
| void | **[[AddPlayerDummyBots]]**(int32 InNumBots) |
| void | **[[AddPlayerNullBots]]**(int32 InNumBots) |
| void | **[[AddStageProgress]]**([FStageActorProgress](/docs/SDK/Source/Classes/structFStageActorProgress.md) Progress) |
| void | **[[AddStageTime]]**(float TimeMinutes) |
| void | **[[AutoBalanceByNumPlayers]]**() |
| void | **[[AutoBalanceByPlayerKills]]**() |
| void | **[[AwardFFAVictory]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * InPlayerVictor) |
| void | **[[AwardVictory]]**(EFaction InVictor, [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * InPlayerVictor) |
| void | **[[BanById]]**(const FString & PlayerId, int32 Hours, const FString & Reason) |
| void | **[[BanByName]]**(const FString & PlayerName, int32 Hours, const FString & Reason) |
| void | **[[BeginEpilogue]]**() |
| void | **[[BroadcastChat]]**(AActor * Sender, const FString & Msg, TEnumAsByte< EChatType::Type > Type, FColor OverrideColor) |
| void | **[[BroadcastLocalizedChat]]**(const FText & Msg, TEnumAsByte< EChatType::Type > Type) |
| void | **[[BroadcastLocalizedChatForFaction]]**(EFaction ReceivingFaction, const FText & Msg, TEnumAsByte< EChatType::Type > Type) |
| void | **[[ClearAllObjectiveAITags]]**() |
| void | **[[ClearPS5MatchId]]**() |
| void | **[[ClearPS5MatchResponsiblePlayer]]**() |
| void | **[[ClearStageProgress]]**([FStageActorProgress](/docs/SDK/Source/Classes/structFStageActorProgress.md) Progress) |
| void | **[[ClientAddMainMenuMessage]]**(const FText & Message) |
| void | **[[DisableSpawningBots]]**() |
| [USpawnQueuer](/docs/SDK/Source/Classes/classUSpawnQueuer.md) * | **[[FindSpawnQueue]]**(FName SpawnQueueName) const |
| TArray< AActor * > | **[[GetAIObjectiveActors]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) const |
| float | **[[GetEpilogueDuration]]**() const |
| TSoftClassPtr< UUserWidget > | **[[GetGameModeWidgetClass]]**() const |
| int32 | **[[GetNumberOfPlayersOnFaction]]**(EFaction Faction, bool bRequirePlayerState) const |
| FString | **[[GetServerDisplayName]]**() |
| FString | **[[GetServerIdentifier]]**() |
| void | **[[HandleAIPossessedPawn]]**([ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) * AIC, APawn * APawn) |
| void | **[[InitSpawnQueuers]]**() |
| void | **[[InitTeams]]**() |
| bool | **[[IsAutoBalanceBlocked]]**() const |
| bool | **[[IsSpawnWaveInQueue]]**(const [ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * SpawnWave) const |
| bool | **[[IsValidHorseCompatibleServer]]**() |
| UObject * | **[[K2_GetCurrentStage]]**() const |
| void | **[[K2_HandleMatchHasStarted]]**() |
| void | **[[K2_HandleMatchIsWaitingToStart]]**() |
| void | **[[K2_HandlePrepareMatch]]**() |
| void | **[[K2_HandleSkipStage]]**() |
| void | **[[KickAllPlayers]]**() |
| void | **[[KickById]]**(const FString & PlayerId, const FString & Reason, float Time) |
| void | **[[KickByName]]**(const FString & PlayerName, const FString & Reason, int32 BanTime) |
| void | **[[KickByNetIdWithTimer]]**(const FUniqueNetIdRepl & UniqueId, const FString & Reason, float BanTime) |
| void | **[[OverrideAIBehavior]]**(const FString & BehaviorTreeName) |
| void | **[[PerformDeferredSpawnRequest]]**([FPendingSpawn](/docs/SDK/Source/Classes/structFPendingSpawn.md) DeferredSpawn) |
| bool | **[[PlayerRequestBeginSpectating]]**(AController * Controller) |
| bool | **[[PlayerRequestNewTeam]]**(AController * Controller, [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * Team, bool bImmediatelySwitch) |
| void | **[[RemoveBots]]**(bool bRemoveLevelBots, bool bRemoveBackfillBots) |
| void | **[[RemoveSessionBan]]**([FSessionBannedPlayer](/docs/SDK/Source/Classes/structFSessionBannedPlayer.md) BannedPlayer) |
| void | **[[SetPS5MatchId]]**(const FString & NewPS5MatchId) |
| void | **[[SetPS5MatchResponsiblePlayer]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * NewPlayerState) |
| void | **[[Slomo]]**(float T) |
| void | **[[TBSAddStageTime]]**(float TimeMinutes) |
| void | **[[TBSEndGame]]**(int32 WinningTeam) |
| void | **[[TBSEndWarmup]]**() |
| void | **[[TBSManuallyStartGame]]**() |
| void | **[[TBSModifyTeamScore]]**(int32 TeamId, int32 Score) |
| void | **[[TBSSetUseMapList]]**(bool UseMapList) |
| void | **[[TBSSkipStage]]**() |
| void | **[[UpdateBotBackfill]]**(int32 NewNumPlayers) |
| void | **[[UpdatePS5MatchResponsibility]]**(APlayerController * ExcludePlayer) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[GetCharacterPerformanceTestInfo]]**(bool & IsRunningTest, int32 & TestIndex) |
| void | **[[NotifyRoundTimeOut]]**() |
| void | **[[OnPCPossessedPawn]]**(APawn * APawn) |
| void | **[[PlayerReadyToSpawn]]**([USpawnQueuer](/docs/SDK/Source/Classes/classUSpawnQueuer.md) * SpawnQueuer, AController * Player, [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * Spawner) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| UBehaviorTree * | **[[AIBehaviorTree]]**  |
| TSubclassOf< [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) > | **[[AIControllerClass]]**  |
| [ATBLActor](/docs/SDK/Source/Classes/classATBLActor.md) * | **[[AlwaysOnMusicManager]]**  |
| EFaction | **[[AttackingFaction]]**  |
| float | **[[AutoBalanceGracePeriodSeconds]]**  |
| TSoftClassPtr< [UBlueprintDebugMenuComponent](/docs/SDK/Source/Classes/classUBlueprintDebugMenuComponent.md) > | **[[BlueprintDebugMenuComponentClass]]**  |
| bool | **[[BotBackfillEnabled]]**  |
| int32 | **[[BotBackfillHighBots]]**  |
| int32 | **[[BotBackfillHighPlayers]]**  |
| int32 | **[[BotBackfillLowBots]]**  |
| int32 | **[[BotBackfillLowPlayers]]**  |
| FCleanupAbilityActors | **[[CleanupAbilityActors]]**  |
| [UContextVOManager](/docs/SDK/Source/Classes/classUContextVOManager.md) * | **[[ContextVOManager]]**  |
| TEnumAsByte< EGameModeType::Type > | **[[CreateGameModeType]]**  |
| TArray< [ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * > | **[[DebugDrawAllTracers]]**  |
| TSubclassOf< [AHorse](/docs/SDK/Source/Classes/classAHorse.md) > | **[[DefaultHorseClass]]**  |
| EFaction | **[[DefendingFaction]]**  |
| TSubclassOf< [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) > | **[[FFATeam]]**  |
| [FRespawnStinger](/docs/SDK/Source/Classes/structFRespawnStinger.md) | **[[FirstSpawnSound]]**  |
| TArray< [AGameModeModifier](/docs/SDK/Source/Classes/classAGameModeModifier.md) * > | **[[GameModeModifiers]]**  |
| TSubclassOf< [UTBLGameModeSettings](/docs/SDK/Source/Classes/classUTBLGameModeSettings.md) > | **[[GameModeSettingsClass]]**  |
| TSubclassOf< [ATBLGameScoringInfo](/docs/SDK/Source/Classes/classATBLGameScoringInfo.md) > | **[[GameScoringClass]]**  |
| [ATBLGameScoringInfo](/docs/SDK/Source/Classes/classATBLGameScoringInfo.md) * | **[[GameScoringInfo]]**  |
| TEnumAsByte< EGameModeType::Type > | **[[GamemodeType]]**  |
| float | **[[IdleKickTimerDisconnect]]**  |
| float | **[[IdleKickTimerSpectate]]**  |
| bool | **[[IgnoreClassLimits]]**  |
| [FMatchComplete](/docs/SDK/Source/Classes/structFMatchComplete.md) | **[[MatchCompleteEvent]]**  |
| FGuid | **[[MatchID]]**  |
| FControllerLogout | **[[OnControllerLogin]]**  |
| FControllerLogout | **[[OnControllerLogout]]**  |
| FHorseKilled | **[[OnHorseKilled]]**  |
| FPawnDowned | **[[OnPawnDowned]]**  |
| FPawnRevived | **[[OnPawnRevived]]**  |
| FPlayerKilled | **[[OnPlayerKilled]]**  |
| FPlayerPossessed | **[[OnPlayerPossessed]]**  |
| AActor * | **[[OverrideAIObjective]]**  |
| float | **[[PostGameSlomo]]**  |
| [FRespawnStinger](/docs/SDK/Source/Classes/structFRespawnStinger.md) | **[[RespawnSound]]**  |
| float | **[[SeamlessTravelEndTime]]**  |
| UCurveFloat * | **[[SecondsBetweenWavesPlayerCountBonus]]**  |
| [FServerPerformanceHistory](/docs/SDK/Source/Classes/structFServerPerformanceHistory.md) | **[[ServerPerformanceHistory]]**  |
| TArray< [FSessionBannedPlayer](/docs/SDK/Source/Classes/structFSessionBannedPlayer.md) > | **[[SessionBannedPlayers]]**  |
| TArray< TSubclassOf< [USpawnQueuer](/docs/SDK/Source/Classes/classUSpawnQueuer.md) > > | **[[SpawnQueuerClasses]]**  |
| TArray< [USpawnQueuer](/docs/SDK/Source/Classes/classUSpawnQueuer.md) * > | **[[SpawnQueuers]]**  |
| TArray< TSubclassOf< [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) > > | **[[Teams]]**  |
| float | **[[TimeBetweenLoadoutVolumeUses]]**  |
| uint8 | **[[bAnalyticsShutdown]]**  |
| bool | **[[bDisablePlayerNamePlates]]**  |
| bool | **[[bFirstBotMatch]]**  |
| bool | **[[bHideHudImportantMessages]]**  |
| bool | **[[bHorseCompatibleServer]]**  |
| bool | **[[bIsFFAGameMode]]**  |
| bool | **[[bLoggingAbilityEvents]]**  |
| bool | **[[bOnlyShowNamesOnTeammates]]**  |
| bool | **[[bPerfomedDeferredSpawnThisFrame]]**  |
| bool | **[[bRespawnImmediately]]**  |
| bool | **[[bUseOpenLoadout]]**  |
| bool | **[[bUsePrioritySpawnSettings]]**  |
| bool | **[[bUseProximitySpawnSettings]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[AutoBalanceKillRelevancyTime]]**  |
| float | **[[AutoBalanceKillThreshold]]**  |
| TArray< [FTeamBalanceConfig](/docs/SDK/Source/Classes/structFTeamBalanceConfig.md) > | **[[AutoBalanceOptions]]**  |
| TArray< [FAutoBalancePlayerSwappingPriorityConfig](/docs/SDK/Source/Classes/structFAutoBalancePlayerSwappingPriorityConfig.md) > | **[[AutoBalancePlayerPriorityConfig]]**  |
| bool | **[[AutoBalancePlayersByKills]]**  |
| bool | **[[AutoBalancePlayersByTeamNumbers]]**  |
| int32 | **[[AutoBalanceTimeUntilForcedRespawn]]**  |
| bool | **[[BlockVoteKicking]]**  |
| TArray< [FClassLimitStruct](/docs/SDK/Source/Classes/structFClassLimitStruct.md) > | **[[ClassLimits]]**  |
| float | **[[DesiredPlayersToStartPercentage]]**  |
| float | **[[EpilogueDuration]]**  |
| TSoftClassPtr< UUserWidget > | **[[GameModeWidgetClass]]**  |
| float | **[[GameModeXPMultiplier]]**  |
| TArray< int32 > | **[[GoldAwardByTeamPlacement]]**  |
| int32 | **[[GoldAwardByTimePeriodAmount]]**  |
| int32 | **[[GoldAwardTimePeriod]]**  |
| int32 | **[[GoldMaxFromPlaytimePerGame]]**  |
| TArray< float > | **[[GoldMultiplierByDailyHour]]**  |
| double | **[[GoldMultiplierByDailyHourTimeDilation]]**  |
| int32 | **[[MapListIndex]]**  |
| TArray< FString > | **[[Maplist]]**  |
| float | **[[MaxTimeBeforeStartingMatch]]**  |
| int32 | **[[MinPlayers]]**  |
| float | **[[MinTimeBeforeStartingMatch]]**  |
| float | **[[MinimumKillsModifierForAutoBalance]]**  |
| int32 | **[[PostMatchTime]]**  |
| float | **[[PrepareMatchDuration]]**  |
| FTimerHandle | **[[PrepareMatchTimerHandle]]**  |
| FString | **[[ServerIdentifier]]**  |
| FString | **[[ServerName]]**  |
| int32 | **[[StartOfMatchGracePeriodForAutoBalance]]**  |
| int32 | **[[StartOfMatchGracePeriodForTeamSwitching]]**  |
| TArray< [FTeamBalanceConfig](/docs/SDK/Source/Classes/structFTeamBalanceConfig.md) > | **[[TeamBalanceOptions]]**  |
| [FTeamImbalanceTracker](/docs/SDK/Source/Classes/structFTeamImbalanceTracker.md) | **[[TeamImbalanceTracker]]**  |
| int32 | **[[TimeBetweenPlayerNumBalanceChecks]]**  |
| int32 | **[[TimeBetweenTeamKillBalanceChecks]]**  |
| float | **[[TimeEnteredWaitingToStart]]**  |
| EFaction | **[[Victor]]**  |
| int32 | **[[XpAwardByTimePeriodAmount]]**  |
| int32 | **[[XpAwardTimePeriod]]**  |
| int32 | **[[XpMaxFromPlaytimePerGame]]**  |
| TArray< float > | **[[XpMultiplierByDailyHour]]**  |
| double | **[[XpMultiplierByDailyHourTimeDilation]]**  |
| bool | **[[bClientSideWeaponTracers]]**  |
| bool | **[[bEnableAutoDemoRecording]]**  |
| bool | **[[bIsAITestMap]]**  |
| bool | **[[bManuallyStartMatch]]**  |
| bool | **[[bSpectatorsCannotSendToAllChat]]**  |
| bool | **[[bUseMaplist]]**  |
| bool | **[[bUsePrepareMatchTimer]]**  |
| bool | **[[bUseStrictTeamBalanceEnforcement]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200
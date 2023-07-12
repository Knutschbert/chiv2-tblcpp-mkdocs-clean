---
title: ATBLGameState
type: class
aliases: ATBLGameState
share: false

---

# ATBLGameState





Inherits from AGameState, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

Inherited by [AArenaGameState](/docs/SDK/Source/Classes/classAArenaGameState.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLGameState]]**() |
| void | **[[AddObjectivePointEvent]]**(EFaction Faction, int32 PointValue, TEnumAsByte< EObjectivePointCategory::Type > Category) |
| void | **[[AddStagePersistentGameModeMessages]]**(TArray< [FGameModeMessage](/docs/SDK/Source/Classes/structFGameModeMessage.md) > NewMessages) |
| void | **[[BroadcastDestroyTornOffItem]]**(FName TornOffName) |
| void | **[[BroadcastPlayerKilled]]**([FDeathEvent](/docs/SDK/Source/Classes/structFDeathEvent.md) DeathEvent) |
| void | **[[BroadcastSetEpicEndGameState]]**(const [FEpicEndGameState](/docs/SDK/Source/Classes/structFEpicEndGameState.md) & InEpicEndGameState) |
| int32 | **[[CalculateEndOfMatchCommodity]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * Player, const FString & Key) |
| float | **[[ConvertServerTimeToLocalTime]]**(float ServerTime) |
| int32 | **[[GetArchetypeCount]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > CharacterClass) |
| int32 | **[[GetArchetypeMaxCount]]**(UObject * WorldContextObject, TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > CharacterClass, EFaction Faction) |
| float | **[[GetCinematicPlaybackTime]]**() |
| TScriptInterface< [IStageInterface](/docs/SDK/Source/Classes/classIStageInterface.md) > | **[[GetCurrentStage]]**() const |
| TSoftClassPtr< UUserWidget > | **[[GetGameModeWidgetClass]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| float | **[[GetLocalPostMatchMatchmakingStartTime]]**() |
| int32 | **[[GetNumObjectivePointsByCategory]]**(EFaction Faction, TEnumAsByte< EObjectivePointCategory::Type > Category) |
| float | **[[GetPostMatchTimeRemaining]]**() |
| float | **[[GetPreparingMatchTimeRemaining]]**() const |
| float | **[[GetServerTimeDifference]]**() |
| TArray< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > > | **[[GetSpawnableClasses]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * LocalPlayer, EFaction Faction) |
| TArray< EFaction > | **[[GetSpawnableTeams]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * LocalPlayerState) |
| float | **[[GetStageTimeRemaining]]**() |
| int32 | **[[GetSubClassCount]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > CharacterClass) |
| int32 | **[[GetSubClassMaxCount]]**(UObject * WorldContextObject, TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > CharacterClass, EFaction Faction) |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[GetTeamWithFaction]]**(EFaction Faction) const |
| float | **[[GetWarmupTimeRemaining]]**() const |
| bool | **[[IsCurrentStage]]**(AActor * Stage) const |
| bool | **[[IsMatchWaitingToStart]]**() |
| bool | **[[IsPostMatch]]**() |
| bool | **[[IsServerBadFrameTime]]**() |
| bool | **[[IsWaitingForAdminToStart]]**() |
| bool | **[[IsWaitingForMinPlayersToStart]]**() |
| void | **[[NotifyCinematicStartedPlayingTryBinding]]**() |
| void | **[[OnRep_CinematicState]]**() |
| void | **[[OnRep_ClassLimits]]**() |
| void | **[[OnRep_FactionContextObjectiveMessage]]**() |
| void | **[[OnRep_GameModeType]]**() |
| void | **[[OnRep_PS5MatchId]]**() |
| void | **[[OnRep_PS5MatchResponsiblePlayer]]**() |
| void | **[[OnRep_SequenceBindings]]**() |
| void | **[[OnRep_StageEndingMusic]]**() |
| void | **[[OnRep_Victor]]**() |
| void | **[[PlayCinematicsWithBinding]]**(ALevelSequenceActor * DefenderSequence, ALevelSequenceActor * AttackerSequence, TMap< [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) *, FString > InSpawnerPrefixes) |
| void | **[[PlayerKilled]]**(AController * Killer, AController * Killed, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource, [FDeathEvent](/docs/SDK/Source/Classes/structFDeathEvent.md) DeathEvent, const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| void | **[[RemoteStageEndingMusic]]**() |
| void | **[[ResetStagePersistentGameModeMessages]]**() |
| void | **[[SetCinematicMode]]**(ECinematicGameState State, ALevelSequenceActor * DefenderSequence, ALevelSequenceActor * AttackerSequence) |
| void | **[[SetGameModeType]]**(TEnumAsByte< EGameModeType::Type > InGameModeType) |
| void | **[[SetObjectiveContextText]]**([FObjectiveContextMessage](/docs/SDK/Source/Classes/structFObjectiveContextMessage.md) NewContextObjectiveMessage) |
| void | **[[SetStageEndingMusic]]**([FAKAudioStartStopStruct](/docs/SDK/Source/Classes/structFAKAudioStartStopStruct.md) Music) |
| void | **[[SetStageTimeRemaining]]**(float TimeInSeconds) |
| bool | **[[ShouldShowLoadoutOnFirstDeath]]**() |
| bool | **[[ShouldShowLoadoutOnPreparingMatch]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| ALevelSequenceActor * | **[[AttackerCinematicSequence]]**  |
| ECinematicGameState | **[[CinematicState]]**  |
| TArray< [FClassLimitStruct](/docs/SDK/Source/Classes/structFClassLimitStruct.md) > | **[[ClassLimits]]**  |
| [FObjectiveContextMessage](/docs/SDK/Source/Classes/structFObjectiveContextMessage.md) | **[[ContextObjectiveMessage]]**  |
| ALevelSequenceActor * | **[[DefenderCinematicSequence]]**  |
| [FEpicEndGameState](/docs/SDK/Source/Classes/structFEpicEndGameState.md) | **[[EpicEndGameState]]**  |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[FFATeam]]**  |
| float | **[[FinalMatchDuration]]**  |
| [FRespawnStinger](/docs/SDK/Source/Classes/structFRespawnStinger.md) | **[[FirstSpawnSound]]**  |
| FText | **[[GameModeName]]**  |
| UDataTable * | **[[GameScoringDataTable]]**  |
| TEnumAsByte< EGameModeType::Type > | **[[GamemodeType]]**  |
| TSoftClassPtr< ULocalMessage > | **[[GameplayEventMessageClass]]**  |
| FString | **[[LobbyId]]**  |
| FText | **[[MapName]]**  |
| int32 | **[[MinPlayersToStart]]**  |
| float | **[[MinRespawnTime]]**  |
| [FTeamScoreEvent](/docs/SDK/Source/Classes/structFTeamScoreEvent.md) | **[[MostRecentTeamScoreEvent]]**  |
| TSubclassOf< [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) > | **[[NeutralTeamClass]]**  |
| FString | **[[NextMapName]]**  |
| UDataTable * | **[[NoveltyScoreDataTable]]**  |
| TArray< [FObjectivePointEntry](/docs/SDK/Source/Classes/structFObjectivePointEntry.md) > | **[[ObjectivePointArray]]**  |
| FNewCharacterSpawned | **[[OnCharacterSpawned]]**  |
| FCinematicGameStateChanged | **[[OnCinematicGameStateChanged]]**  |
| FStartEpicEndGameEventSignature | **[[OnEpicEndGameEvent]]**  |
| FMatchEndedSignature | **[[OnMatchEnded]]**  |
| FMatchStartedSignature | **[[OnMatchStarted]]**  |
| FMatchStateChanged | **[[OnMatchStateChanged]]**  |
| FMatchWonBySignature | **[[OnMatchWonBy]]**  |
| FNewObjecitveContextMessage | **[[OnNewObjectiveContextMessage]]**  |
| FPS5MatchIdUpdated | **[[OnPS5MatchIdUpdated]]**  |
| FGameStatePlayerKilled | **[[OnPlayerKilled]]**  |
| FPlayerStateAdded | **[[OnPlayerStateAdded]]**  |
| FPlayerStateKillsUpdated | **[[OnPlayerStateKillsUpdated]]**  |
| FPlayerStateRemoved | **[[OnPlayerStateRemoved]]**  |
| FPlayerStateUniqueIdReplicated | **[[OnPlayerStateUniqueIdReplicated]]**  |
| FCinematicPlayingStateBegun | **[[OnPlayingStateBegun]]**  |
| FPostMatchEndTimeChanged | **[[OnPostMatchEndTimeChanged]]**  |
| FString | **[[PS5MatchId]]**  |
| FUniqueNetIdRepl | **[[PS5MatchResponsiblePlayer]]**  |
| FString | **[[Platform]]**  |
| [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * | **[[PlayerVictor]]**  |
| int32 | **[[PlayersNeededToStartEarly]]**  |
| int32 | **[[ProgressBarPrimaryTeamIndex]]**  |
| TArray< [FReplSequenceBinding](/docs/SDK/Source/Classes/structFReplSequenceBinding.md) > | **[[ReplicatedSequenceBindings]]**  |
| [FRespawnStinger](/docs/SDK/Source/Classes/structFRespawnStinger.md) | **[[RespawnSound]]**  |
| float | **[[ServerCinematicStartTime]]**  |
| FText | **[[ServerName]]**  |
| float | **[[ServerTimeDifference]]**  |
| float | **[[StageEndTime]]**  |
| [FAKAudioStartStopStruct](/docs/SDK/Source/Classes/structFAKAudioStartStopStruct.md) | **[[StageEndingMusic]]**  |
| TArray< [FGameModeMessage](/docs/SDK/Source/Classes/structFGameModeMessage.md) > | **[[StagePersistentGameModeMessages]]**  |
| TArray< [FStageActorProgress](/docs/SDK/Source/Classes/structFStageActorProgress.md) > | **[[StageProgressList]]**  |
| float | **[[StageStartTime]]**  |
| UDataTable * | **[[TeamScoreFormatDataTable]]**  |
| TArray< [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * > | **[[Teams]]**  |
| EFaction | **[[Victor]]**  |
| [UVotingManagerComponent](/docs/SDK/Source/Classes/classUVotingManagerComponent.md) * | **[[VotingManagerComponent]]**  |
| uint8 | **[[bBadFrameTimePerformance]]**  |
| uint8 | **[[bBadNetworkPerformance]]**  |
| uint8 | **[[bClientSideWeaponTracers]]**  |
| bool | **[[bDisablePlayerNamePlates]]**  |
| bool | **[[bDisableSpawningBots]]**  |
| bool | **[[bDisableTeamSelect]]**  |
| bool | **[[bHideHudImportantMessages]]**  |
| bool | **[[bIsGameModeFFA]]**  |
| bool | **[[bOnlyShowNamesOnTeammates]]**  |
| bool | **[[bServerBadFrameTime]]**  |
| bool | **[[bUseOpenLoadout]]**  |
| bool | **[[bUsingNewSpawnSystem]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200
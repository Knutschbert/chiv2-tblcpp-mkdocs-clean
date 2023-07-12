---
title: ASpawnWave
type: class
aliases: ASpawnWave
share: false

---

# ASpawnWave





Inherits from [ATBLActor](/docs/SDK/Source/Classes/classATBLActor.md), AActor, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

Inherited by [AForcedRespawnSpawnWave](/docs/SDK/Source/Classes/classAForcedRespawnSpawnWave.md), [AForwardSpawnWave](/docs/SDK/Source/Classes/classAForwardSpawnWave.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ASpawnWave]]**() |
| void | **[[AllowFullPlayerControl]]**() |
| void | **[[AttemptCleanup]]**() |
| void | **[[End]]**() |
| void | **[[FireEarly]]**() |
| TArray< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > > | **[[GetAllowedCharacterClasses]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * TargetController) |
| TSubclassOf< [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) > | **[[GetAllowedLoadoutSelection]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > RequestedClass) |
| void | **[[GetDisplayInfo]]**(TMap< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) >, TSubclassOf< [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) >> & AllowedClasses, UTexture2D *& SpawnWaveIcon, FText & SpawnWaveName, bool & SpawnWithHorse) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| int32 | **[[GetNumberOfJoinedPlayers]]**() |
| float | **[[GetTimeLeft]]**(AController * Target) const |
| void | **[[HandleNoLongerJoinable]]**() |
| bool | **[[HasPendingDeferredSpawnsRemaining]]**() const |
| bool | **[[IsJoinableBy]]**(AController * Controller) |
| bool | **[[IsPlayerInSpawnWave]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PS) |
| bool | **[[IsSpecialSpawn]]**() |
| bool | **[[JoinSpawn]]**(AController * Controller) |
| bool | **[[LeaveSpawn]]**(AController * Controller) |
| bool | **[[NeedsCleanup]]**() const |
| void | **[[NotifyPendingDeferredSpawn]]**() |
| void | **[[NotifyPendingDeferredSpawnPerformed]]**() |
| void | **[[OnRep_WaveState]]**() |
| void | **[[ProcessInitiallySpawnedCharacters]]**([ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * InstigatorSpawner, const TArray< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > & Characters) |
| void | **[[Public_StartSpawning]]**() |
| bool | **[[RejectSpawn]]**(AController * Controller) |
| void | **[[ReportSpawnFailure]]**(AController * Controller, const FName & Reason) |
| void | **[[SetClientJoinTime]]**(float InClientJoinWorldTime) |
| void | **[[SetNoLongerJoinable]]**() |
| bool | **[[ShouldShowSpawnPrompt]]**() |
| void | **[[SpawnController]]**(AController * Controller) |
| void | **[[StartCleanupTimer]]**(bool bRestart) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnControllerPossessedPawn]]**(APawn * NewPawn) |
| void | **[[OnRep_ReplJoinedPlayers]]**() |
| void | **[[StartPrespawning]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[ExtraSecondsBeforeSpawningToSpawnBots]]**  |
| EFaction | **[[Faction]]**  |
| TSet< AController * > | **[[JoinedPlayers]]**  |
| float | **[[LastPendingDeferredSpawnRequest]]**  |
| int32 | **[[MaxPlayerCount]]**  |
| float | **[[MinimumWaitTimeSeconds]]**  |
| FPossessedCharacter | **[[OnPossessedCharacter]]**  |
| FSpawnWaveSpawnedCharacter | **[[OnSpawnedCharacter]]**  |
| FWaveFilled | **[[OnWaveFilled]]**  |
| FWaveFinished | **[[OnWaveFinished]]**  |
| FWaveFinished | **[[OnWaveNoLongerJoinable]]**  |
| FWaveSpawning | **[[OnWaveSpawning]]**  |
| int32 | **[[PendingDeferredSpawnCount]]**  |
| TArray< AController * > | **[[PlayersToSpawn]]**  |
| float | **[[PrespawnTime]]**  |
| TSet< AController * > | **[[RejectedPlayers]]**  |
| TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > | **[[ReplJoinedPlayers]]**  |
| float | **[[SecondsBeforeSpawningStarts]]**  |
| float | **[[SecondsJoinableAfterSpawningStarts]]**  |
| [FSpawnWaveSounds](/docs/SDK/Source/Classes/structFSpawnWaveSounds.md) | **[[SpawnWaveSounds]]**  |
| [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * | **[[Spawner]]**  |
| TSubclassOf< [USpecialSpawnSpec](/docs/SDK/Source/Classes/classUSpecialSpawnSpec.md) > | **[[SpecialSpawnSpec]]**  |
| float | **[[StartTime]]**  |
| ESpawnWaveState | **[[WaveState]]**  |
| bool | **[[bAllowBots]]**  |
| bool | **[[bControlRestricted]]**  |
| uint8 | **[[bFireWhenFilled]]**  |
| bool | **[[bForcedSpawn]]**  |
| bool | **[[bForwardSpawn]]**  |
| bool | **[[bIsPlayFromHere]]**  |
| bool | **[[bPrespawn]]**  |
| bool | **[[bPrivateWave]]**  |
| bool | **[[bWantsEndAfterControlReturned]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| USceneComponent * | **[[DummyRoot]]**  |
| TSet< AController * > | **[[HistoryOfJoinedPlayers]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200
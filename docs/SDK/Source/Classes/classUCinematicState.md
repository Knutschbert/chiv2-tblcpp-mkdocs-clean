---
title: UCinematicState
type: class
aliases: UCinematicState
share: false

---

# UCinematicState





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BeginState]]**(FGameplayTag PreviousState) |
| void | **[[EndState]]**(FGameplayTag NextState) |
| [UCinematicsComponent](/docs/SDK/Source/Classes/classUCinematicsComponent.md) * | **[[GetCinematicsComponent]]**() const |
| [ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * | **[[GetPlayerController]]**() const |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[GetTBLCharacter]]**() const |
| void | **[[HandleCharacterAllowControl]]**() |
| void | **[[HandleCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatState) |
| void | **[[HandleGameCinematicStateChanged]]**(ECinematicGameState GameStateCinematicState) |
| void | **[[HandleGoingToSpawnAtSpawner]]**([ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * Spawner) |
| void | **[[HandleMatchStateChanged]]**(FName MatchState) |
| void | **[[HandleNextSpawnTeamChanged]]**([ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * NewTeam) |
| void | **[[HandleNextSpawnWaveChanged]]**([ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * SpawnWave) |
| void | **[[HandlePendingSpawn]]**([ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * PendingSpawner, float ServerSpawnTimeSeconds) |
| void | **[[HandlePossessedPawn]]**(APawn * Pawn) |
| void | **[[HandleSuicideNotify]]**(EKillReason KillReason) |
| void | **[[HandleTeamChanged]]**([ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * NewTeam) |
| void | **[[HandleUIStateChanged]]**(FGameplayTag UIState) |
| void | **[[HideLoadingScreen]]**() |
| void | **[[Tick]]**(float DeltaTime) |
| | **[[UCinematicState]]**() |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200
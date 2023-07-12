---
title: AForwardSpawnWave
type: class
aliases: AForwardSpawnWave
share: false

---

# AForwardSpawnWave





Inherits from [ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md), [ATBLActor](/docs/SDK/Source/Classes/classATBLActor.md), AActor, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AForwardSpawnWave]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| bool | **[[IsControllerRecentlyInCombat]]**(AController * Controller) const |
| void | **[[SetAwaitingCombatTimer]]**(AController * Controller) |
| void | **[[SetPawnsAllowedToForwardSpawn]]**(TArray< APawn * > InPawnsAllowedToForwardSpawn) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ForwardSpawnController]]**(AController * Controller) |
| void | **[[OnQueuedPlayerCauseDamage]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnQueuedPlayerParryEvent]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * A, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * B, [FParryEventState](/docs/SDK/Source/Classes/structFParryEventState.md) ParryEventState) |
| void | **[[OnQueuedPlayerTakeDamage]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnRep_PawnsAllowedToForwardSpawn]]**() |
| void | **[[ResetCombatTimerFor]]**(AController * Controller) |
| bool | **[[ShouldResetCombatTimerFor]]**(AController * Controller) const |
| void | **[[SpawnOutOfCombatCharacters]]**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TSet< APawn * > | **[[AllowedPawns]]**  |
| float | **[[CombatTimerDuration]]**  |
| TSet< TWeakObjectPtr< AController > > | **[[ControllerAwaitingCombatTimer]]**  |
| TMap< TWeakObjectPtr< AController >, FTimerHandle > | **[[ControllerCombatTimerMap]]**  |
| TMap< TWeakObjectPtr< AController >, FTimerHandle > | **[[ControllerTimerMap]]**  |
| TArray< APawn * > | **[[PawnsAllowedToForwardSpawn]]**  |
| TSet< APawn * > | **[[RejectedPawns]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200
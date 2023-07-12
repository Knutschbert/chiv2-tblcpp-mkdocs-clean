---
title: AOutOfCombatZoneAuthority
type: class
aliases: AOutOfCombatZoneAuthority
share: false

---

# AOutOfCombatZoneAuthority





Inherits from AActor, [IMatchStateListenerInterface](/docs/SDK/Source/Classes/classIMatchStateListenerInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AOutOfCombatZoneAuthority]]**() |
| bool | **[[CanHaveForgivenessTime]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) const |
| void | **[[CancelForgivenessTimer]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| float | **[[GetCurrentLowestTimeLeft]]**(const TArray< [AOutOfCombatZoneAuthority](/docs/SDK/Source/Classes/classAOutOfCombatZoneAuthority.md) * > & Authorities, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| float | **[[GetForgivenessTime]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) const |
| float | **[[GetTimerDelaySeconds]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, bool & OutIsInForgivenessTime) const |
| void | **[[HandleCharacterSpawned]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| bool | **[[IsInForgivenessTime]]**(ACharacter * Character) const |
| void | **[[OnActionTriggered]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[OnBeginOverlap]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[OnEndOverlap]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[OnForgivenessTimerElapsed]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[OnLocalPlayerBeginOverlap]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[OnLocalPlayerEndOverlap]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| bool | **[[ShouldIgnoreCharacter]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) const |
| void | **[[StartForgivenessTimer]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, FTimerHandle & TimerHandle) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[HandleActionTimerFired]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[HandleBeginOverlap]]**(AActor * OverlappedActor, AActor * OtherActor) |
| void | **[[HandleCharacterDestroyed]]**(AActor * DestroyedActor) |
| void | **[[HandleEndOverlap]]**(AActor * OverlappedActor, AActor * OtherActor) |
| void | **[[HandleLocalControllerPlayerStateReplicated]]**(APlayerState * PS) |
| void | **[[HandleLocalControllerPossessedPawn]]**(APawn * Pawn) |
| void | **[[HandleOnArenaRoundWon]]**(EFaction Winner) |
| void | **[[HandleOnPlayerKilled]]**([FDeathEvent](/docs/SDK/Source/Classes/structFDeathEvent.md) DeathEvent) |
| bool | **[[K2_ShouldIgnoreCharacter]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [AOutOfCombatZoneVolume](/docs/SDK/Source/Classes/classAOutOfCombatZoneVolume.md) * > | **[[ActiveVolumes]]**  |
| TSet< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > | **[[CharactersThatLeftMe]]**  |
| TSet< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > | **[[CharactersThatSpawnedInMe]]**  |
| float | **[[HorseRecentSpawnForgivenessSeconds]]**  |
| float | **[[HorseTimerDelaySeconds]]**  |
| FCombatZoneEventSignature | **[[OnActionTriggeredEvent]]**  |
| FCombatVolumeEventSignature | **[[OnActiveVolumesChanged]]**  |
| FCombatZoneEventSignature | **[[OnBeginOverlapEvent]]**  |
| FCombatZoneEventSignature | **[[OnEndOverlapEvent]]**  |
| FCombatZoneEventSignature | **[[OnLocalPlayerBeginOverlapEvent]]**  |
| FCombatZoneEventSignature | **[[OnLocalPlayerEndOverlapEvent]]**  |
| TMap< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) *, [FVolumeSet](/docs/SDK/Source/Classes/structFVolumeSet.md) > | **[[Overlaps]]**  |
| float | **[[RecentSpawnForgivenessSeconds]]**  |
| float | **[[TimerDelaySeconds]]**  |
| bool | **[[bInverted]]**  |
| bool | **[[bIsLocalPlayerOverlapping]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TMap< ACharacter *, FTimerHandle > | **[[ActionTimerHandles]]**  |
| TSet< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > > | **[[ConsideredCharacters]]**  |
| TMap< ACharacter *, FTimerHandle > | **[[ForgivenessTimerHandles]]**  |
| TSet< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > > | **[[IgnoredCharacters]]**  |
| bool | **[[bDisabled]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200
---
title: USpecialSpawnSpec
type: class
aliases: USpecialSpawnSpec
share: false

---

# USpecialSpawnSpec





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[CanSpawnHorse]]**([ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * SpawnWave) const |
| bool | **[[ForceBotsUseLoadout]]**() const |
| TSubclassOf< [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) > | **[[GetAllowedClassLoadout]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > CharacterClass) const |
| TMap< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) >, TSubclassOf< [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) > > | **[[GetAllowedClasses]]**() const |
| void | **[[GetAllowedClassesList]]**(TArray< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) >> & AllowedClassesList, [ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * TargetController) const |
| void | **[[GetAllowedClassesSet]]**(TSet< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) >> & AllowedClassesSet, [ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * TargetController) const |
| int32 | **[[GetMaxHorseCount]]**([ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * SpawnWave, EFaction FactionOverride) const |
| TSubclassOf< [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) > | **[[GetRandomClassLoadout]]**() const |
| bool | **[[HasAllowedClassList]]**() const |
| bool | **[[IsAllowedClass]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > CharacterClass) const |
| bool | **[[IsHorseWave]]**() const |
| | **[[USpecialSpawnSpec]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[AutoVoAllyCavalaryIncomingDelay]]**  |
| float | **[[AutoVoCavalaryChargeDelay]]**  |
| float | **[[AutoVoEnemyCavalryIncomingDelay]]**  |
| float | **[[AutoVoHorseAllyPercent]]**  |
| float | **[[AutoVoHorseEnemyPercent]]**  |
| float | **[[AutoVoOffenseChargeDelay]]**  |
| FText | **[[SpawnName]]**  |
| UTexture2D * | **[[SpawnWaveIcon]]**  |
| bool | **[[bAutospawnAllowed]]**  |
| bool | **[[bForceBotsUseLoadout]]**  |
| bool | **[[bIgnorePlayerOwnership]]**  |
| bool | **[[bJoinAfterDeath]]**  |
| bool | **[[bPromptedSpawn]]**  |
| bool | **[[bUseSubclassesOfAllowedClasses]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TMap< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) >, TSubclassOf< [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) > > | **[[AllowedClasses]]**  |
| int32 | **[[MaxHorseCount]]**  |
| bool | **[[bHorse]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
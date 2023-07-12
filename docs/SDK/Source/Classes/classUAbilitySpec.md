---
title: UAbilitySpec
type: class
aliases: UAbilitySpec
share: false

---

# UAbilitySpec





Inherits from [UAssemblyBlueprint](/docs/SDK/Source/Classes/classUAssemblyBlueprint.md), UBlueprint

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[GetAllChildActions]]**(TArray< [UAction](/docs/SDK/Source/Classes/classUAction.md) * > & outActions) const |
| | **[[UAbilitySpec]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UAbilityActivationMethod](/docs/SDK/Source/Classes/classUAbilityActivationMethod.md) * | **[[ActivationMethod]]**  |
| TArray< [UAction](/docs/SDK/Source/Classes/classUAction.md) * > | **[[AllActions]]**  |
| TArray< [UCondition](/docs/SDK/Source/Classes/classUCondition.md) * > | **[[AllConditions]]**  |
| TArray< [UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md) * > | **[[AllTargetMethods]]**  |
| float | **[[BlueprintCleanupDelayTime]]**  |
| TArray< [FCharacterControlOverTime](/docs/SDK/Source/Classes/structFCharacterControlOverTime.md) > | **[[CharacterControl]]**  |
| EProjectileSpawnType | **[[ProjectileSpawnType]]**  |
| [UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md) * | **[[TargetMethod]]**  |
| bool | **[[bAimAtCrosshair]]**  |
| bool | **[[bInterruptOnDeath]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200
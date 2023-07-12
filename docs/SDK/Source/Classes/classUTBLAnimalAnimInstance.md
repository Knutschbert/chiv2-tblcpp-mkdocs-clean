---
title: UTBLAnimalAnimInstance
type: class
aliases: UTBLAnimalAnimInstance
share: false

---

# UTBLAnimalAnimInstance





Inherits from [UTBLAnimInstance](/docs/SDK/Source/Classes/classUTBLAnimInstance.md), UAnimInstance

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[EventOnKilled]]**() |
| void | **[[EventOnLanded]]**() |
| void | **[[EventOnStartedPanicking]]**() |
| void | **[[EventOnTookDamage]]**() |
| void | **[[NotifyKilled]]**() |
| void | **[[NotifyLanded]]**() |
| void | **[[NotifyStartedPanicking]]**() |
| void | **[[NotifyTookDamage]]**() |
| void | **[[OnAnimationSetChanged]]**(TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > AnimationSet) |
| | **[[UTBLAnimalAnimInstance]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [ATBLAnimal](/docs/SDK/Source/Classes/classATBLAnimal.md) * | **[[Animal]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[AnimationSetBase]]**  |
| float | **[[MoveSpeedSq]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[PreviewAnimationSet]]**  |
| [UStatsComponent](/docs/SDK/Source/Classes/classUStatsComponent.md) * | **[[Stats]]**  |
| float | **[[TimeSinceLastHit]]**  |
| float | **[[TimeStartedPanicking]]**  |
| bool | **[[bIsBeingHeld]]**  |
| bool | **[[bIsBeingHeld_Combat]]**  |
| bool | **[[bIsBeingThrown]]**  |
| bool | **[[bIsDead]]**  |
| bool | **[[bIsMoving]]**  |
| bool | **[[bProcessedDeath]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
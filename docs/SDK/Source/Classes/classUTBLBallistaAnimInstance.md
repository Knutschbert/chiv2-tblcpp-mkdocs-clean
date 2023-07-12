---
title: UTBLBallistaAnimInstance
type: class
aliases: UTBLBallistaAnimInstance
share: false

---

# UTBLBallistaAnimInstance





Inherits from [UTBLAnimInstance](/docs/SDK/Source/Classes/classUTBLAnimInstance.md), UAnimInstance

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnBallistaDismounted]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, EDismountType DismountType) |
| void | **[[OnBallistaMounted]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[OnBallistaRepaired]]**() |
| void | **[[OnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * NewCombatState) |
| void | **[[OnRepaired]]**() |
| | **[[UTBLBallistaAnimInstance]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [ABallista](/docs/SDK/Source/Classes/classABallista.md) * | **[[BallistaActor]]**  |
| float | **[[BallistaPitch]]**  |
| float | **[[BallistaYaw]]**  |
| [UTBLCharacterAnimInstance_Playable](/docs/SDK/Source/Classes/classUTBLCharacterAnimInstance__Playable.md) * | **[[CharacterAnimBP]]**  |
| FName | **[[CombatState]]**  |
| bool | **[[Is3p]]**  |
| bool | **[[IsActive]]**  |
| bool | **[[IsLoaded]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[MountedCharacter]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
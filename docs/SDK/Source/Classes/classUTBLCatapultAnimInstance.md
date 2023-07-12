---
title: UTBLCatapultAnimInstance
type: class
aliases: UTBLCatapultAnimInstance
share: false

---

# UTBLCatapultAnimInstance





Inherits from [UTBLAnimInstance](/docs/SDK/Source/Classes/classUTBLAnimInstance.md), UAnimInstance

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AnimNotify_catapultFireEnd_Action]]**() |
| void | **[[CatapultFireAction]]**() |
| void | **[[CatapultLaunchCharacters]]**() |
| void | **[[OnCatapultDismounted]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, EDismountType DismountType) |
| void | **[[OnCatapultFireNoDriver]]**() |
| void | **[[OnCatapultMounted]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[OnCatapultStateChanged]]**(uint8 State, uint8 PreviousState) |
| void | **[[OnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * NewCombatState) |
| | **[[UTBLCatapultAnimInstance]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [ACatapult](/docs/SDK/Source/Classes/classACatapult.md) * | **[[CatapultActor]]**  |
| [UTBLCharacterAnimInstance_Playable](/docs/SDK/Source/Classes/classUTBLCharacterAnimInstance__Playable.md) * | **[[CharacterAnimBP]]**  |
| float | **[[ChargePercent]]**  |
| FName | **[[CombatState]]**  |
| bool | **[[Is3p]]**  |
| bool | **[[IsActive]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[MountedCharacter]]**  |
| FOnAnimNotifyCatapultFire | **[[OnAnimNotifyCatapultFire]]**  |
| FOnAnimNotifyCatapultFire | **[[OnAnimNotifyCatapultFireEnd]]**  |
| bool | **[[bInteractable]]**  |
| bool | **[[bIsPacked]]**  |
| bool | **[[bWantsToFire]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
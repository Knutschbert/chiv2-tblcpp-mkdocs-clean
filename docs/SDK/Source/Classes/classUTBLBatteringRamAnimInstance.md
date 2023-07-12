---
title: UTBLBatteringRamAnimInstance
type: class
aliases: UTBLBatteringRamAnimInstance
share: false

---

# UTBLBatteringRamAnimInstance





Inherits from [UTBLAnimInstance](/docs/SDK/Source/Classes/classUTBLAnimInstance.md), UAnimInstance

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AnimNotify_ramFire_Action]]**() |
| void | **[[AnimNotify_ramRecovery_End]]**() |
| void | **[[EventOnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| | **[[UTBLBatteringRamAnimInstance]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [ABatteringRam](/docs/SDK/Source/Classes/classABatteringRam.md) * | **[[BatteringRamActor]]**  |
| float | **[[ChargePercent]]**  |
| FName | **[[CombatState]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[LeftCharacter]]**  |
| [UTBLCharacterAnimInstance_Playable](/docs/SDK/Source/Classes/classUTBLCharacterAnimInstance__Playable.md) * | **[[LeftCharacterAnimBP]]**  |
| USkeletalMeshComponent * | **[[LeftCharacterMesh]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[RightCharacter]]**  |
| [UTBLCharacterAnimInstance_Playable](/docs/SDK/Source/Classes/classUTBLCharacterAnimInstance__Playable.md) * | **[[RightCharacterAnimBP]]**  |
| USkeletalMeshComponent * | **[[RightCharacterMesh]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
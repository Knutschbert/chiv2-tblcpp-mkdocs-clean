---
title: UTBLCharacterMountableAnimInstance
type: class
aliases: UTBLCharacterMountableAnimInstance
share: false

---

# UTBLCharacterMountableAnimInstance





Inherits from [UTBLAnimInstance](/docs/SDK/Source/Classes/classUTBLAnimInstance.md), UAnimInstance

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AnimNotify_CharacterFire_Action]]**() |
| void | **[[AnimNotify_CharacterRecovery_End]]**() |
| void | **[[AnimNotify_InFinalMontageSection]]**() |
| void | **[[AnimNotify_MountableActorKilledAnim_End]]**() |
| void | **[[EventOnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[EventOnKilled]]**() |
| void | **[[MountableActorDeadOnStartup]]**() |
| void | **[[OnAnimationStart]]**() |
| void | **[[OnHealthChanged]]**(float Amount, AActor * Initiator) |
| | **[[UTBLCharacterMountableAnimInstance]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [ACharacterMountableActor](/docs/SDK/Source/Classes/classACharacterMountableActor.md) * | **[[CharacterMountedableActor]]**  |
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
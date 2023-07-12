---
title: UTBLBombardAnimInstance
type: class
aliases: UTBLBombardAnimInstance
share: false

---

# UTBLBombardAnimInstance





Inherits from [UTBLAnimInstance](/docs/SDK/Source/Classes/classUTBLAnimInstance.md), UAnimInstance

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AddLogEntry]]**(const FString & LogEntry) |
| void | **[[OnBombardDismounted]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, EDismountType DismountType) |
| void | **[[OnBombardFireAction]]**() |
| void | **[[OnBombardFireActionBegin]]**() |
| void | **[[OnBombardMounted]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[OnBombardRepaired]]**() |
| void | **[[OnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * NewCombatState) |
| void | **[[OnRepaired]]**() |
| | **[[UTBLBombardAnimInstance]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [ABombard](/docs/SDK/Source/Classes/classABombard.md) * | **[[BombardActor]]**  |
| float | **[[BombardPitch]]**  |
| float | **[[BombardYaw]]**  |
| [UTBLCharacterAnimInstance_Playable](/docs/SDK/Source/Classes/classUTBLCharacterAnimInstance__Playable.md) * | **[[CharacterAnimBP]]**  |
| FName | **[[CombatState]]**  |
| bool | **[[Is3p]]**  |
| bool | **[[IsActive]]**  |
| bool | **[[IsLoaded]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[MountedCharacter]]**  |
| FOnAnimNotifyBombardFire | **[[OnAnimNotifyBombardFire]]**  |
| FOnBombardFireAnimComplete | **[[OnBombardFireAnimComplete]]**  |
| bool | **[[bWantsToFire]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
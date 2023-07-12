---
title: UTBLWeaponAnimInstance
type: class
aliases: UTBLWeaponAnimInstance
share: false

---

# UTBLWeaponAnimInstance





Inherits from [UTBLAnimInstance](/docs/SDK/Source/Classes/classUTBLAnimInstance.md), UAnimInstance

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AnimNotify_ShowArrow]]**() |
| void | **[[EndWeaponAnimation]]**() |
| void | **[[EventOnCombatStateChanged]]**(FName PreviousState, FName NewState) |
| void | **[[OnAnimationSetChanged]]**(FName AnimSetName, [FAnimationSetDataTable](/docs/SDK/Source/Classes/structFAnimationSetDataTable.md) AnimInfo, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * InInventoryItem) |
| void | **[[OnAttackMontageSectionChanged]]**(UAnimMontage * Montage, int32 NextSection) |
| void | **[[OnDropped]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, FTransform Transform) |
| void | **[[StartWeaponAnimation]]**() |
| | **[[UTBLWeaponAnimInstance]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[AnimationSetBase]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[AnimationSetBase1P]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[AnimationSetBase3P]]**  |
| FName | **[[AttackName]]**  |
| FName | **[[CombatState]]**  |
| TMap< FName, FName > | **[[IdlePoses]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[InventoryItem]]**  |
| bool | **[[Is3p]]**  |
| bool | **[[IsAddedToInventory]]**  |
| bool | **[[IsCarryable]]**  |
| bool | **[[IsEquipped]]**  |
| bool | **[[IsLoaded]]**  |
| FName | **[[MontageStartingSection]]**  |
| FName | **[[PreviousCombatState]]**  |
| TArray< FName > | **[[ReloadStates]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
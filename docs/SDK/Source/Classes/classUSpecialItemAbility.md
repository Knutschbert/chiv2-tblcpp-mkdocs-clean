---
title: USpecialItemAbility
type: class
aliases: USpecialItemAbility
share: false

---

# USpecialItemAbility





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ApplyHelperBonus]]**() |
| void | **[[BattlecryAbilityEnd]]**() |
| void | **[[BattlecryAbilityStart]]**() |
| void | **[[FullyRecharge]]**() |
| float | **[[GetCurrentCharge]]**() const |
| float | **[[GetMaxCharge]]**() const |
| int32 | **[[GetPerkBonus]]**() const |
| void | **[[OnDamageCaused]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & Event) |
| void | **[[OnDamageTaken]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & Event) |
| void | **[[OnEquippedItemsChanged]]**() |
| void | **[[OnItemStackChanged]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, int32 Delta) |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & Event) |
| void | **[[OnParrySuccess]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * ThisCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * OtherCharacter, [FParryEventState](/docs/SDK/Source/Classes/structFParryEventState.md) ParryEventState) |
| void | **[[OnPawnRevived]]**(APawn * RevivedPlayer, APawn * RevivorPlayer) |
| void | **[[OnRechargeTimer]]**() |
| void | **[[OnStartHeal]]**(AActor * HealedActor, EHealingSource HealingSource) |
| void | **[[OnUseItem]]**() |
| | **[[USpecialItemAbility]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[DecreaseStackCount]]**() |
| void | **[[IncreaseStackCount]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[MaxCharge]]**  |
| FBattleCryChargeUpdated | **[[OnChargeUpdated]]**  |
| FOnSpecialItemEquip | **[[OnSpecialItemEquip]]**  |
| FOnSpecialItemUsed | **[[OnSpecialItemUseFailed]]**  |
| FOnSpecialItemUsed | **[[OnSpecialItemUsed]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[SpecialItem]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[CurrentCharge]]**  |
| ESpecialItemChargeType | **[[LastChargeType]]**  |
| EEquippedState | **[[LastEquippedState]]**  |
| int32 | **[[LastStackCount]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[OwnerCharacter]]**  |
| uint8 | **[[bIsUsing]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
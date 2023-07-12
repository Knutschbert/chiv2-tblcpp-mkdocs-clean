---
title: UPerksComponent
type: class
aliases: UPerksComponent
share: false

---

# UPerksComponent





Inherits from UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AddTemporaryPerk]]**(ETemporaryPerkType TempPerkType) |
| bool | **[[HasPerk]]**(EPerkType PerkType) const |
| void | **[[RemoveTemporaryPerk]]**(ETemporaryPerkType TempPerkType) |
| | **[[UPerksComponent]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ApplyHelperBonus]]**() |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & Event) |
| void | **[[OnPawnRevived]]**(APawn * RevivedPlayer, APawn * RevivorPlayer) |
| void | **[[OnStartHeal]]**(AActor * HealedActor, EHealingSource HealingSource) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[BackstabAngle]]**  |
| UCurveFloat * | **[[HealCurve]]**  |
| float | **[[HealSpeed]]**  |
| UDataTable * | **[[PerksDataTable]]**  |
| UDataTable * | **[[TemporaryPerksDataTable]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[CurrentClass]]**  |
| TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[CurrentSubclass]]**  |
| float | **[[EagerBonusDamage]]**  |
| TMap< EPerkType, FName > | **[[EnumToName]]**  |
| float | **[[HelperHealthBonus]]**  |
| float | **[[OneHandWeaponSpeedBonus]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[OwnerCharacter]]**  |
| float | **[[SapperBonusDamage]]**  |
| float | **[[SneakyBonusDamage]]**  |
| float | **[[SniperBonusDamage]]**  |
| TMap< ETemporaryPerkType, float > | **[[TemporaryPerkValues]]**  |
| TArray< ETemporaryPerkType > | **[[TemporaryPerks]]**  |
| uint8 | **[[bHasEagerBonus]]**  |
| uint8 | **[[bHasSapperBonus]]**  |
| uint8 | **[[bHasSneakyBonus]]**  |
| uint8 | **[[bHasSniperBonus]]**  |
| uint8 | **[[bHasSprintAttack]]**  |
| uint8 | **[[bHasSprintCharge]]**  |
| uint8 | **[[bHasSprintShove]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
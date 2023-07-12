---
title: ABatteringRam
type: class
aliases: ABatteringRam
share: false

---

# ABatteringRam





Inherits from [ASiegeEngine](/docs/SDK/Source/Classes/classASiegeEngine.md), [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md), [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), [IDamagerInterface](/docs/SDK/Source/Classes/classIDamagerInterface.md), ACharacter, [ISignificanceInterface](/docs/SDK/Source/Classes/classISignificanceInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ABatteringRam]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| int32 | **[[GetNumCharacters]]**() const |
| void | **[[OnPushableActivated]]**(bool bIsActive) |
| void | **[[OnRep_ChargePercent]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnCharacterDismounted]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DismountedDriver, EDismountType DismountType) |
| void | **[[OnCharacterMount]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[OnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatState) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[ChargePercent]]**  |
| float | **[[ChargeTime]]**  |
| [UCombatStateComponent](/docs/SDK/Source/Classes/classUCombatStateComponent.md) * | **[[CombatStateComponent]]**  |
| [UCombatStateQueue](/docs/SDK/Source/Classes/classUCombatStateQueue.md) * | **[[CombatStateQueue]]**  |
| TSubclassOf< [UCombatStateSet](/docs/SDK/Source/Classes/classUCombatStateSet.md) > | **[[CombatStateSet]]**  |
| [UCombatStateSynchronization](/docs/SDK/Source/Classes/classUCombatStateSynchronization.md) * | **[[CombatStateSynchronization]]**  |
| UCurveFloat * | **[[DamageScale]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[LeftInteractable]]**  |
| [USiegeMountPoint](/docs/SDK/Source/Classes/classUSiegeMountPoint.md) * | **[[LeftMountPoint]]**  |
| FOnChargeChanged | **[[OnChargeChanged]]**  |
| [UPushableComponent](/docs/SDK/Source/Classes/classUPushableComponent.md) * | **[[PushableComponent]]**  |
| UPhysicsAsset * | **[[PushablePhysAsset]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[RightInteractable]]**  |
| [USiegeMountPoint](/docs/SDK/Source/Classes/classUSiegeMountPoint.md) * | **[[RightMountPoint]]**  |
| UPhysicsAsset * | **[[StationaryPhysAsset]]**  |
| float | **[[TwoPlayerChargeBonus]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200
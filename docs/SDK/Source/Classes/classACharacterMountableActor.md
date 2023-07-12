---
title: ACharacterMountableActor
type: class
aliases: ACharacterMountableActor
share: false

---

# ACharacterMountableActor





Inherits from [ASiegeEngine](/docs/SDK/Source/Classes/classASiegeEngine.md), [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md), [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), [IDamagerInterface](/docs/SDK/Source/Classes/classIDamagerInterface.md), ACharacter, [ISignificanceInterface](/docs/SDK/Source/Classes/classISignificanceInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ACharacterMountableActor]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| int32 | **[[GetNumCharacters]]**() const |
| UPrimitiveComponent * | **[[GetPushingComponent]]**() const |
| bool | **[[NeedsTick]]**() const |
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
| FName | **[[AbilityAttackName]]**  |
| FName | **[[AbilityChargeName]]**  |
| FName | **[[CharacterMountableActorAnimName]]**  |
| float | **[[ChargePercent]]**  |
| float | **[[ChargeTime]]**  |
| UCurveFloat * | **[[ChargeToDamageScale]]**  |
| [UCombatStateComponent](/docs/SDK/Source/Classes/classUCombatStateComponent.md) * | **[[CombatStateComponent]]**  |
| [UCombatStateQueue](/docs/SDK/Source/Classes/classUCombatStateQueue.md) * | **[[CombatStateQueue]]**  |
| TSubclassOf< [UCombatStateSet](/docs/SDK/Source/Classes/classUCombatStateSet.md) > | **[[CombatStateSet]]**  |
| [UCombatStateSynchronization](/docs/SDK/Source/Classes/classUCombatStateSynchronization.md) * | **[[CombatStateSynchronization]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[LeftInteractable]]**  |
| [USiegeMountPoint](/docs/SDK/Source/Classes/classUSiegeMountPoint.md) * | **[[LeftMountPoint]]**  |
| float | **[[MinimumChargePercent]]**  |
| FOnAnimationStarting | **[[OnAnimationStarting]]**  |
| FOnCharacterChargeChanged | **[[OnChargeChanged]]**  |
| FOnFinalMontageSectionPlaying | **[[OnFinalMontageSectionPlaying]]**  |
| FOnMountableActorKilledAnimComplete | **[[OnMountableActorKilledAnimComplete]]**  |
| UPhysicsAsset * | **[[PhysAsset]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[RightInteractable]]**  |
| [USiegeMountPoint](/docs/SDK/Source/Classes/classUSiegeMountPoint.md) * | **[[RightMountPoint]]**  |
| float | **[[TwoPlayerChargeBonus]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TWeakObjectPtr< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[AbilityInstigatingDriver]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200
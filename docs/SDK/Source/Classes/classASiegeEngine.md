---
title: ASiegeEngine
type: class
aliases: ASiegeEngine
share: false

---

# ASiegeEngine





Inherits from [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md), [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), [IDamagerInterface](/docs/SDK/Source/Classes/classIDamagerInterface.md), ACharacter, [ISignificanceInterface](/docs/SDK/Source/Classes/classISignificanceInterface.md)

Inherited by [ABallista](/docs/SDK/Source/Classes/classABallista.md), [ABatteringRam](/docs/SDK/Source/Classes/classABatteringRam.md), [ABombard](/docs/SDK/Source/Classes/classABombard.md), [ACatapult](/docs/SDK/Source/Classes/classACatapult.md), [ACharacterMountableActor](/docs/SDK/Source/Classes/classACharacterMountableActor.md), [AHorse](/docs/SDK/Source/Classes/classAHorse.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ASiegeEngine]]**() |
| void | **[[ArrowCamGamePadPressed]]**() |
| void | **[[ArrowCamGamePadReleased]]**() |
| void | **[[ArrowCamPressed]]**() |
| void | **[[ArrowCamReleased]]**() |
| void | **[[BroadcastSetRotationYaw]]**(float NewRotationYaw) |
| void | **[[DismountPressed]]**() |
| void | **[[DismountReleased]]**() |
| void | **[[Fire]]**() |
| void | **[[FireReleased]]**() |
| void | **[[ForceDismount]]**(EDismountType DismountType) |
| float | **[[GetChargingPercent]]**() |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[GetDriver]]**() |
| EFaction | **[[GetLastDriverFaction]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| AActor * | **[[GetLoadedItem]]**() const |
| float | **[[GetMinChargingToFire]]**() |
| [UCombatStateComponent](/docs/SDK/Source/Classes/classUCombatStateComponent.md) * | **[[GetSiegeEngineCombatStateComponent]]**() |
| bool | **[[IsLoaded]]**() const |
| void | **[[MountPressed]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[OnAbilityError]]**(AActor * Initiator, TEnumAsByte< EResultCode::Type > Code, [AAbilityInvocation](/docs/SDK/Source/Classes/classAAbilityInvocation.md) * Invocation, FName AttackName, TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > ItemClass) |
| void | **[[OnDriverKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnDriverSetRagdollPhysics]]**() |
| void | **[[OnRiderCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatState) |
| void | **[[OnTurnLockLimit]]**(float DeltaTime, float DeltaYaw) |
| void | **[[UseKeyPressed]]**() |
| void | **[[UseKeyReleased]]**() |
| void | **[[UseKeyRepeat]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BroadcastDismount]]**(EDismountType DismountType) |
| void | **[[BroadcastInterpToMountLocation]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[BroadcastMount]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| bool | **[[CanMount]]**(APawn * Pawn) |
| void | **[[FocusPressed]]**() |
| void | **[[FocusReleased]]**() |
| void | **[[OnRep_Driver]]**() |
| void | **[[ServerDismountPressed]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| AActor * | **[[AIAimHintLocation]]**  |
| AAIController * | **[[AIController]]**  |
| bool | **[[AllowEmoteAnimations]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[AnimationSet]]**  |
| UAkComponent * | **[[AudioComponent]]**  |
| FName | **[[CameraAttachSocketName]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[CharacterAnimationSet]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[CharacterAnimationSet1P]]**  |
| FName | **[[CharacterAttachSocketName]]**  |
| TArray< EWeaponAbilitySlotKey > | **[[DisableAbilitySlot]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[Driver]]**  |
| AController * | **[[DriverController]]**  |
| FName | **[[FireAbilityName]]**  |
| FOnDriverDismount | **[[OnDriverDismount]]**  |
| FOnDriverMount | **[[OnDriverMount]]**  |
| FCatapultLoadedAmmo | **[[OnLoadedAmmo]]**  |
| FCatapultReadyToFire | **[[OnReadyToFire]]**  |
| float | **[[PitchRotationLimit]]**  |
| [FReplicationPredictionState](/docs/SDK/Source/Classes/structFReplicationPredictionState.md) | **[[PredictionState]]**  |
| float | **[[RotationYaw]]**  |
| FName | **[[SiegeEngineName]]**  |
| ESiegeEngineType | **[[SiegeEngineType]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[SiegeInventoryItem]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[SiegeInventoryItemClass]]**  |
| [FTurnLimitSound](/docs/SDK/Source/Classes/structFTurnLimitSound.md) | **[[TurnLimitSound]]**  |
| float | **[[YawRotationLimit]]**  |
| bool | **[[bCompressRotationYaw]]**  |
| bool | **[[bFireHeld]]**  |
| bool | **[[bUseRotationYaw]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[GamepadUsePressedTime]]**  |
| EFaction | **[[LastDriverFaction]]**  |
| [FMountBlendParams](/docs/SDK/Source/Classes/structFMountBlendParams.md) | **[[MountBlendParams]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[ReplicatedDriver]]**  |
| TArray< USceneComponent * > | **[[SiegeMountPointList]]**  |
| TArray< FName > | **[[ValidCombatStates]]**  |
| bool | **[[bNeedToInitializeTBLCharacter]]**  |
| bool | **[[bUseDismountCombatState]]**  |
| bool | **[[bUseMountCombatState]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200
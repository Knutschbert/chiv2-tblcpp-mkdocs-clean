---
title: ACatapult
type: class
aliases: ACatapult
share: false

---

# ACatapult





Inherits from [ASiegeEngine](/docs/SDK/Source/Classes/classASiegeEngine.md), [ILoadItemInterface](/docs/SDK/Source/Classes/classILoadItemInterface.md), [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md), [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), [IDamagerInterface](/docs/SDK/Source/Classes/classIDamagerInterface.md), ACharacter, [ISignificanceInterface](/docs/SDK/Source/Classes/classISignificanceInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ACatapult]]**() |
| void | **[[BroadcastFireNoDriver]]**() |
| void | **[[CatapultLoadItem]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Initiator) |
| void | **[[EventUsePressed]]**(APawn * InPawn, [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * InInteractable) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| UPrimitiveComponent * | **[[GetLoadVolume]]**() |
| UPrimitiveComponent * | **[[GetReloadCollision]]**() |
| UPrimitiveComponent * | **[[GetSpoonCollision]]**() |
| bool | **[[IsInteractable]]**() const |
| bool | **[[IsPackaged]]**() const |
| bool | **[[IsPushable]]**() const |
| void | **[[K2_OnCatapultStateChanged]]**(ECatapultState State, ECatapultState PreviousState) |
| void | **[[OnFire]]**() |
| void | **[[OnRep_CatapultState]]**(ECatapultState PreviousState) |
| void | **[[OnRep_ChargePercent]]**() |
| void | **[[OnRep_LoadedAmmo]]**() |
| void | **[[OnRep_RotationSpeed]]**() |
| void | **[[ReloadPressed]]**() |
| void | **[[ReloadReleased]]**() |
| void | **[[RemoveAttachedItem]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| void | **[[SetCatapultState]]**(ECatapultState State) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[CanLoad]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| void | **[[ClientOnFire]]**() |
| bool | **[[IsCatapultRock]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| void | **[[OnDamageTaken]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & Event) |
| void | **[[OnHealthChanged]]**(float Amount, AActor * Initiator) |
| void | **[[OnItemPickup]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, bool IsAddedToInventory) |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & Event) |
| void | **[[OnLoadVolumeBeginOverlap]]**(UPrimitiveComponent * OverlappedComponent, AActor * Other, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult & OverlapInfo) |
| void | **[[OnLoadVolumeEndOverlap]]**(UPrimitiveComponent * OverlappedComponent, AActor * OtherActor, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex) |
| void | **[[OnPushableActivated]]**(bool IsActive) |
| void | **[[OnReloadCollision]]**(UPrimitiveComponent * OverlappedComponent, AActor * Other, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult & OverlapInfo) |
| void | **[[OnRep_Broken]]**() |
| void | **[[ReadyToFire]]**() |
| void | **[[ServerFirePressed]]**() |
| void | **[[ServerFireReleased]]**() |
| void | **[[ServerReloadPressed]]**() |
| void | **[[ServerReloadReleased]]**() |
| void | **[[SetBroken]]**(bool bInBroken) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UAbilitiesComponent](/docs/SDK/Source/Classes/classUAbilitiesComponent.md) * | **[[Abilities]]**  |
| TSubclassOf< UAnimInstance > | **[[AnimationBlueprint]]**  |
| TArray< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * > | **[[AttachedItems]]**  |
| float | **[[AutoLoadFacingAngle]]**  |
| float | **[[BaseTurnRate]]**  |
| UAnimationAsset * | **[[BrokenAnimation]]**  |
| USkeletalMesh * | **[[BrokenMesh]]**  |
| UParticleSystem * | **[[BrokenParticle]]**  |
| [FProjectileSounds](/docs/SDK/Source/Classes/structFProjectileSounds.md) | **[[CatapultProjectileSoundOverride]]**  |
| int32 | **[[ChargeIncrements]]**  |
| float | **[[ChargePercent]]**  |
| [FSiegeEngineDamageSounds](/docs/SDK/Source/Classes/structFSiegeEngineDamageSounds.md) | **[[DamageSounds]]**  |
| USkeletalMesh * | **[[DamagedMesh]]**  |
| float | **[[DamagedThreshold]]**  |
| UPhysicsAsset * | **[[DestroyedPhysAsset]]**  |
| TArray< UAkAudioEvent * > | **[[FiringSounds]]**  |
| USkeletalMesh * | **[[HealthyMesh]]**  |
| uint8 | **[[IsBeingRotated]]**  |
| UAkAudioEvent * | **[[ItemLoadedSound]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[LastLoadedAmmo]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[LoadedAmmo]]**  |
| TWeakObjectPtr< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) > | **[[LoadedAmmoInstigator]]**  |
| FName | **[[LoadedAmmoSocketName]]**  |
| float | **[[MaxDrawStrength]]**  |
| float | **[[MinChargeTime]]**  |
| float | **[[MinChargeToFire]]**  |
| float | **[[MinDrawStrength]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[MountInteractable]]**  |
| UAkAudioEvent * | **[[MountSound]]**  |
| float | **[[NextChargeIncrement]]**  |
| FOnCatapultDamagedMeshApplied | **[[OnCatapultDamagedMeshApplied]]**  |
| FCatapultFireNoDriver | **[[OnCatapultFireNoDriver]]**  |
| FOnCatapultKilled | **[[OnCatapultKilled]]**  |
| FCatapultStateChanged | **[[OnCatapultStateChanged]]**  |
| FCatapultChargePercentChanged | **[[OnChargePercentChanged]]**  |
| FOnCatapultRepaired | **[[OnRepaired]]**  |
| UAkAudioEvent * | **[[PlayReloadLoopSound]]**  |
| UAkAudioEvent * | **[[PlayTurnLoopSound]]**  |
| float | **[[PreviousChargeIncrement]]**  |
| UPhysicsAsset * | **[[PushablePhysAsset]]**  |
| [UPushingComponent](/docs/SDK/Source/Classes/classUPushingComponent.md) * | **[[PushingComponent]]**  |
| int32 | **[[PushingPriority]]**  |
| UAkAudioEvent * | **[[ReadyToFireSound]]**  |
| float | **[[RemainingChargeTime]]**  |
| [URepairableComponent](/docs/SDK/Source/Classes/classURepairableComponent.md) * | **[[Repairable]]**  |
| UPhysicsAsset * | **[[StationaryPhysAsset]]**  |
| [UStatsComponent](/docs/SDK/Source/Classes/classUStatsComponent.md) * | **[[Stats]]**  |
| UAkAudioEvent * | **[[StopReloadLoopSound]]**  |
| UAkAudioEvent * | **[[StopTurnLoopSound]]**  |
| TArray< TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > > | **[[WhitelistAmmoItemTypes]]**  |
| bool | **[[bEnforceYawRotationLimitOnCatapult]]**  |
| bool | **[[bFocusHeld]]**  |
| bool | **[[bIsCharging]]**  |
| bool | **[[bIsFiring]]**  |
| bool | **[[bIsUnwinding]]**  |
| bool | **[[bOverrideDrawStrength]]**  |
| bool | **[[bReloadHeld]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TWeakObjectPtr< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[BlockedAutoLoadCharacter]]**  |
| ECatapultState | **[[CatapultState]]**  |
| int32 | **[[HorizLockId]]**  |
| FVector_NetQuantize10 | **[[InitialRotation]]**  |
| FRotator | **[[LastAimRotation]]**  |
| [FProjectileSounds](/docs/SDK/Source/Classes/structFProjectileSounds.md) | **[[LoadedAmmoProjectileBackupSounds]]**  |
| TArray< USceneComponent * > | **[[LoadingComponentList]]**  |
| TArray< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > | **[[OverlappingCharacters]]**  |
| int32 | **[[VertLockId]]**  |
| bool | **[[bIsBroken]]**  |
| bool | **[[bReplicatedIsBroken]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200
---
title: ABallista
type: class
aliases: ABallista
share: false

---

# ABallista





Inherits from [ASiegeEngine](/docs/SDK/Source/Classes/classASiegeEngine.md), [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md), [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), [IDamagerInterface](/docs/SDK/Source/Classes/classIDamagerInterface.md), ACharacter, [ISignificanceInterface](/docs/SDK/Source/Classes/classISignificanceInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ABallista]]**() |
| void | **[[EventUsePressed]]**(APawn * InPawn, [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * InInteractable) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| void | **[[OnRep_Broken]]**() |
| void | **[[OnRep_RotationSpeed]]**() |
| void | **[[SetBroken]]**(bool bInBroken) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnDamageTaken]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & Event) |
| void | **[[OnHealthChanged]]**(float Amount, AActor * Initiator) |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & Event) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UAbilitiesComponent](/docs/SDK/Source/Classes/classUAbilitiesComponent.md) * | **[[Abilities]]**  |
| FName | **[[AmmoAttachSocketName]]**  |
| TSubclassOf< UAnimInstance > | **[[AnimationBlueprint]]**  |
| UAnimationAsset * | **[[BrokenAnimation]]**  |
| USkeletalMesh * | **[[BrokenMesh]]**  |
| UParticleSystem * | **[[BrokenParticle]]**  |
| [FSiegeEngineDamageSounds](/docs/SDK/Source/Classes/structFSiegeEngineDamageSounds.md) | **[[DamageSounds]]**  |
| USkeletalMesh * | **[[DamagedMesh]]**  |
| float | **[[DamagedThreshold]]**  |
| TArray< UAkAudioEvent * > | **[[FiringSounds]]**  |
| USkeletalMesh * | **[[HealthyMesh]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[Interactable]]**  |
| FOnBallistaKilled | **[[OnBallistaKilled]]**  |
| FOnRepaired | **[[OnRepaired]]**  |
| UAkAudioEvent * | **[[ReloadSound]]**  |
| uint8 | **[[RemoteViewYaw]]**  |
| [URepairableComponent](/docs/SDK/Source/Classes/classURepairableComponent.md) * | **[[Repairable]]**  |
| float | **[[RotationSpeed]]**  |
| [UStatsComponent](/docs/SDK/Source/Classes/classUStatsComponent.md) * | **[[Stats]]**  |
| float | **[[TurnLimitStrength]]**  |
| UAkAudioEvent * | **[[TurningSoundAKEvent]]**  |
| bool | **[[bIsBroken]]**  |
| uint8 | **[[bLoaded]]**  |
| uint8 | **[[bRepaired]]**  |
| bool | **[[bReplicatedIsBroken]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| int32 | **[[HorizLockId]]**  |
| FRotator | **[[LastAimRotation]]**  |
| FRotator | **[[LastControlRotation]]**  |
| float | **[[RotationWeight]]**  |
| float | **[[RotationWeightInterpSpeed]]**  |
| int32 | **[[TurnRateId]]**  |
| int32 | **[[VertLockId]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200
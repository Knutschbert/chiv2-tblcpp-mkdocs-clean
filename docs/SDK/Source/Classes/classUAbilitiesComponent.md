---
title: UAbilitiesComponent
type: class
aliases: UAbilitiesComponent
share: false

---

# UAbilitiesComponent





Inherits from [UTBLComponent](/docs/SDK/Source/Classes/classUTBLComponent.md), [IInstancedObjectContainer](/docs/SDK/Source/Classes/classIInstancedObjectContainer.md), UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [FResult](/docs/SDK/Source/Classes/structFResult.md) | **[[CanInitiate]]**([UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * Spec) |
| void | **[[ClientAbilityInitiated]]**(const [FClientAbilityInitiationParams](/docs/SDK/Source/Classes/structFClientAbilityInitiationParams.md) & Params) |
| void | **[[ClientAbilityInvocationComplete]]**(int32 InvocationId) |
| void | **[[ClientSpamTest]]**(const FString & Payload) |
| void | **[[ClientStartTargetMethodCosmetic]]**([UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * AbilitySpec, int32 InvocationId, [FAbilityInitiationParams](/docs/SDK/Source/Classes/structFAbilityInitiationParams.md) InitiationParams, [UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md) * TargetMethod) |
| [FAbility](/docs/SDK/Source/Classes/structFAbility.md) | **[[GetAbility]]**([UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * Spec) |
| [FResult](/docs/SDK/Source/Classes/structFResult.md) | **[[InitiateAbility]]**([UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * Spec, [FAbilityInitiationParams](/docs/SDK/Source/Classes/structFAbilityInitiationParams.md) InitiationParams) |
| void | **[[OnInvocationComplete]]**([AAbilityInvocation](/docs/SDK/Source/Classes/classAAbilityInvocation.md) * Invocation, [UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * AbilitySpec) |
| void | **[[RemoveInvocationActor]]**([UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * AbilitySpec, TEnumAsByte< EInvocationScope::Type > Scope, AActor * Actor) |
| void | **[[ServerCombatStateStartAttack]]**([UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * AbilitySpec, const [FCombatStateStartAttack](/docs/SDK/Source/Classes/structFCombatStateStartAttack.md) & Params) |
| void | **[[ServerInitiateAbility]]**(const [FServerInitiateAbilityParams](/docs/SDK/Source/Classes/structFServerInitiateAbilityParams.md) & Params) |
| void | **[[ServerTerminateAbility]]**([UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * AbilitySpec) |
| void | **[[SyncServerInitiateAbility]]**(const [FServerInitiateAbilityParams](/docs/SDK/Source/Classes/structFServerInitiateAbilityParams.md) & Params) |
| [FResult](/docs/SDK/Source/Classes/structFResult.md) | **[[TerminateAbility]]**([UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * Spec) |
| | **[[UAbilitiesComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FAbilityArray](/docs/SDK/Source/Classes/structFAbilityArray.md) | **[[Abilities]]**  |
| TArray< [UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * > | **[[AbilityGrants]]**  |
| [UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * | **[[InitiatingAbility]]**  |
| FAbilityAdded | **[[OnAdded]]**  |
| FAbilityErrorSignature | **[[OnError]]**  |
| FAbilityInitiatedSignature | **[[OnInitiated]]**  |
| FAbilityOnCooldown | **[[OnOnCooldown]]**  |
| FAbilityRemoved | **[[OnRemoved]]**  |
| FTargetMethodFinishedSignature | **[[OnTargetMethodFinished]]**  |
| int32 | **[[Version]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200
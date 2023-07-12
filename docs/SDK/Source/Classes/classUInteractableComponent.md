---
title: UInteractableComponent
type: class
aliases: UInteractableComponent
share: false

---

# UInteractableComponent





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), [IDisplayComponentInterface](/docs/SDK/Source/Classes/classIDisplayComponentInterface.md)

Inherited by [UDestroyableComponent](/docs/SDK/Source/Classes/classUDestroyableComponent.md), [URepairableComponent](/docs/SDK/Source/Classes/classURepairableComponent.md), [UWeaponRackComponent](/docs/SDK/Source/Classes/classUWeaponRackComponent.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[CanShowUI]]**(APawn * Pawn) const |
| bool | **[[GetEnabled]]**() |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[GetInteractableComponent]]**() |
| EInteractionType | **[[GetInteractionType]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| EInteractableRechargeRule | **[[GetRechargeRule]]**() |
| EFaction | **[[GetUseableByTeam]]**() |
| int32 | **[[GetUses]]**() |
| TArray< UPrimitiveComponent * > | **[[GetValidCollisionComponents]]**() const |
| bool | **[[IsValidCollisionComponent]]**(UPrimitiveComponent * Component) |
| void | **[[OnRep_InitiateUseDuration]]**() |
| void | **[[OnRep_InteractionType]]**() |
| void | **[[OnRep_RechargeRule]]**() |
| void | **[[OnRep_Uses]]**() |
| void | **[[RestartRechargeTimer]]**() |
| void | **[[SetEnabled]]**(bool Enabled, bool bForceClient) |
| void | **[[SetInitiateUseDuration]]**(float InInitiateUseDuration) |
| void | **[[SetInteractionType]]**(EInteractionType InInteractionType) |
| void | **[[SetOnlyAllowOwningPlayer]]**(bool bInOnlyAllowOwningPlayer) |
| void | **[[SetRechargeRule]]**(EInteractableRechargeRule InRechargeRule) |
| void | **[[SetUseableByTeam]]**(EFaction EFaction) |
| void | **[[StopRechargeTimer]]**() |
| | **[[UInteractableComponent]]**() |
| void | **[[Use]]**(APawn * Pawn) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FText | **[[ActorName]]**  |
| EFaction | **[[AllowedTeam]]**  |
| TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[CharacterClassRequiredToUse]]**  |
| TSoftClassPtr< [UHUDContainerSubWidget](/docs/SDK/Source/Classes/classUHUDContainerSubWidget.md) > | **[[ConfigWidgetClass]]**  |
| float | **[[Cooldown]]**  |
| float | **[[CurrentCooldownTime]]**  |
| float | **[[CurrentUseTime]]**  |
| [FReplicated_AActorPtr](/docs/SDK/Source/Classes/structFReplicated__AActorPtr.md) | **[[CurrentUsingPawn]]**  |
| float | **[[DecayRate]]**  |
| FText | **[[Description]]**  |
| int32 | **[[InitialUses]]**  |
| float | **[[InitiateUseDuration]]**  |
| EInteractCombatState | **[[InteractCombatState]]**  |
| EInteractionType | **[[InteractionType]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[ItemRequiredToUse]]**  |
| FName | **[[KeyBind]]**  |
| int32 | **[[MaxUses]]**  |
| FInteractableComponentCanBeUsed | **[[OnCanBeUsed]]**  |
| FInteractableComponentCanShowUI | **[[OnCanShowUI]]**  |
| FInteractableComponentOnCooldownSignature | **[[OnCooldown]]**  |
| FInteractableComponentOnUsesChangedSignature | **[[OnInteracbleUsesUpdated]]**  |
| FInteractableComponentOnInteractableEnabled | **[[OnInteractableEnabled]]**  |
| FInteractableComponentOnInteractableFocusedSignature | **[[OnInteractableFocused]]**  |
| FInteractableComponentOnInteractableLostFocusSignature | **[[OnInteractableLostFocus]]**  |
| FInteractableComponentOnInteractableReachableSignature | **[[OnInteractableReachable]]**  |
| FInteractableComponentOnInteractableUnreachableSignature | **[[OnInteractableUnreachable]]**  |
| FUsingPawnChangedSignature | **[[OnPawnChanged]]**  |
| FInteractableComponentOnUseSignature | **[[OnUse]]**  |
| FInteractableComponentOnUseHeldSignature | **[[OnUseHeld]]**  |
| FInteractableComponentOnUseHeldInitiatedSignature | **[[OnUseHeldInitiated]]**  |
| FInteractableComponentOnUseReleasedSignature | **[[OnUseReleased]]**  |
| FInteractableComponentOnUseSignature | **[[OnUseSyncFailed]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[OverrideInteractable]]**  |
| EInteractableRechargeRule | **[[RechargeRule]]**  |
| int32 | **[[RechargeStacks]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[ReplicatedInitiateUseDuration]]**  |
| [FReplicated_EInteractionType](/docs/SDK/Source/Classes/structFReplicated__EInteractionType.md) | **[[ReplicatedInteractionType]]**  |
| [FReplicated_EInteractableRechargeRule](/docs/SDK/Source/Classes/structFReplicated__EInteractableRechargeRule.md) | **[[ReplicatedRechargeRule]]**  |
| [FStageActorAction](/docs/SDK/Source/Classes/structFStageActorAction.md) | **[[StageActorAction]]**  |
| EInteractableUILocation | **[[UILocation]]**  |
| float | **[[UseRechargeTime]]**  |
| [FReplicated_EFaction](/docs/SDK/Source/Classes/structFReplicated__EFaction.md) | **[[UseableByTeam]]**  |
| [FReplicated_Int32](/docs/SDK/Source/Classes/structFReplicated__Int32.md) | **[[Uses]]**  |
| APawn * | **[[UsingPawn]]**  |
| TSet< UPrimitiveComponent * > | **[[ValidCollisionComponentSet]]**  |
| TArray< FName > | **[[ValidCollisionComponents]]**  |
| TSoftClassPtr< [UHUDContainerSubWidget](/docs/SDK/Source/Classes/classUHUDContainerSubWidget.md) > | **[[WidgetClass]]**  |
| bool | **[[bAllowProximityCheck]]**  |
| bool | **[[bAutoPickupOnly]]**  |
| bool | **[[bCheckValidEquipState]]**  |
| bool | **[[bHideInteractablePrompt]]**  |
| bool | **[[bIsUseHeld]]**  |
| bool | **[[bOnCooldown]]**  |
| bool | **[[bOnlyAllowOwningPlayer]]**  |
| bool | **[[bShouldHaveHudMarker]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
---
title: UInventory
type: class
aliases: UInventory
share: false

---

# UInventory





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ApplyBlockedDamage]]**([FInventoryItemDamagedParams](/docs/SDK/Source/Classes/structFInventoryItemDamagedParams.md) Params, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * BlockingItem) |
| void | **[[BroadcastProjectileHitPassiveShield]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Shield, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Projectile) |
| void | **[[BroadcastProjectilePenetratedPassiveShield]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Shield, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Projectile, FVector HitLocation) |
| bool | **[[CanSwitchInventoryItem]]**(FName KeyBind) |
| void | **[[DoBattlecry]]**() |
| void | **[[DoBattlecryAbility]]**() |
| void | **[[DropAllItems]]**() |
| void | **[[DropItem]]**(EInventoryItemSlot Slot, [FDropItemParams](/docs/SDK/Source/Classes/structFDropItemParams.md) Params, bool bDuringParryEvent) |
| void | **[[DropItemOnKilled]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| void | **[[EquipCustomizationItem]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| TArray< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * > | **[[GetAmmoInventoryItems]]**() const |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetAmmoItem]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| float | **[[GetBattleCryHeldProgress]]**() |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetDualWieldOffhand]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetEquippedItemByHand]]**(EEquippedHand Hand) const |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetEquippedItemBySlot]]**(EInventoryItemSlot Slot) const |
| TArray< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * > | **[[GetEquippedItems]]**() const |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetEquippedWeapon]]**() const |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetInventoryItemBySlot]]**(EInventoryItemSlot Slot) |
| TArray< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * > | **[[GetInventoryItemsBySlot]]**(EInventoryItemSlot Slot) |
| FName | **[[GetKeybindName]]**(EInventoryItemSlot Slot) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[GetNoveltyItemClass]]**() |
| void | **[[GetRefillItemsToGrant]]**(TMap< TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) >, int32 > & ItemsToGrant, const TArray< TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) >> & ItemsToRefill, bool RefillAllAmmoItems, bool UseStackCountFromItem, int32 StacksToAdd) |
| float | **[[GetTimeSinceLastTriedBandage]]**() const |
| bool | **[[HasMissingItemsToRefill]]**(const TArray< TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) >> & ItemsToRefill) const |
| bool | **[[IsShieldEquipped]]**() |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| void | **[[PickupItem]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, int32 StackCountToAdd, EPickupEquipOptions EquipOptions, AActor * Initiator, bool bIgnoreStateCheck, bool bGiveWeapon) |
| void | **[[PickupTornOffItem]]**(TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > ItemClass) |
| void | **[[QueueWeaponFlourish]]**() |
| void | **[[RefillItems]]**(TArray< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * > & OutGrantedItems, const TArray< TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) >> & ItemsToRefill, bool RefillAllAmmoItems, bool UseStackCountFromItem, int32 StacksToAdd, bool GrantFullAmmo, EPickupEquipOptions EquipOptions) |
| void | **[[ServerDebugSetAmmo]]**(int32 Ammo) |
| void | **[[SetObjectForItemLoad]]**(UObject * Object) |
| bool | **[[ShowBandageRefillActors]]**() const |
| | **[[UInventory]]**() |
| void | **[[UnequipAllItems]]**(bool bImmediately, bool bPlayUnequip) |
| void | **[[UnequipCustomizationItem]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BroadcastInventoryItemDamaged]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, [FInventoryItemDamagedParams](/docs/SDK/Source/Classes/structFInventoryItemDamagedParams.md) Params) |
| void | **[[ClientIsUnequippingOnMount]]**(bool OnMount) |
| void | **[[ClientUsedItem]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| void | **[[HorseBattleCryPressed]]**() |
| void | **[[InventoryKeyPressed]]**(EInventoryItemSlot Slot) |
| void | **[[InventoryNext]]**() |
| void | **[[InventoryPrevious]]**() |
| void | **[[InventoryPrimary]]**() |
| void | **[[InventoryToggleMainHand]]**() |
| void | **[[OnApplyCondition]]**(AActor * Actor, EConditionType Condition) |
| void | **[[OnCombatStateBegin]]**(AActor * Actor, FName State, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[OnCombatStateEnd]]**(AActor * Actor, FName State, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[OnCombatStateEvent]]**(AActor * Actor, FName EventName, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo) |
| void | **[[OnRemoveCondition]]**(AActor * Actor, EConditionType Condition, AActor * ConditionRemover) |
| void | **[[OnRep_AmmoItems]]**() |
| void | **[[OnRep_DualWieldOffhands]]**() |
| void | **[[OnRep_InventorySlots]]**() |
| void | **[[OnRep_IsUnequippingOnMount]]**() |
| void | **[[OverheadPressed]]**() |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[RemoveItem]]**(EInventoryItemSlot Slot, bool bEndAttack) |
| void | **[[ServerSetObjectForItemLoad]]**(UObject * Object) |
| void | **[[SlashPressed]]**() |
| void | **[[StabPressed]]**() |
| void | **[[SwitchInventoryItem]]**() |
| void | **[[SwitchToBrokenItem]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[BattleCryHeldStartTime]]**  |
| float | **[[BattleCryHeldTime]]**  |
| UDataTable * | **[[EquippedPenaltyTable]]**  |
| float | **[[GamepadBattleCryHeldStartTime]]**  |
| float | **[[GamepadBattleCryHeldTime]]**  |
| int32 | **[[GamepadBattleCryPressedCount]]**  |
| EGamepadBattleCryState | **[[GamepadBattleCryState]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[GamepadBattlecryStartInteractable]]**  |
| float | **[[GamepadHorseBattleCryHeldStartTime]]**  |
| int32 | **[[GamepadHorseBattleCryPressedCount]]**  |
| EGamepadBattleCryState | **[[GamepadHorseBattleCryState]]**  |
| float | **[[GamepadInputDoubleTapWaitTime]]**  |
| float | **[[GamepadInputWaitTime]]**  |
| float | **[[GamepadJabHeldStartTime]]**  |
| float | **[[GamepadJabHeldTime]]**  |
| float | **[[GamepadRightDPadPressedCount]]**  |
| float | **[[GamepadWaitOverheadStartTime]]**  |
| float | **[[GamepadWaitRightDPadStartTime]]**  |
| float | **[[GamepadWaitStabStartTime]]**  |
| UDataTable * | **[[InventoryPenaltyTable]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[ItemToUse]]**  |
| UObject * | **[[ObjectForItemLoad]]**  |
| FOnAddedToInventoryChanged | **[[OnAddedToInventoryChanged]]**  |
| FOnBattleCryStarted | **[[OnBattleCryFinished]]**  |
| FOnBattleCryStarted | **[[OnBattleCryStarted]]**  |
| FOnCharacterEquippedItemsChanged | **[[OnCharacterEquippedItemsChanged]]**  |
| FOnDisabledAttackInput | **[[OnDisabledAttackInput]]**  |
| FOnEquippedItemsChanged | **[[OnEquippedItemsChanged]]**  |
| FOnInventoryActionFailed | **[[OnInventoryActionFailed]]**  |
| FOnInventoryItemDamageStateChanged | **[[OnInventoryItemDamageStateChanged]]**  |
| FOnInventoryItemDamaged | **[[OnInventoryItemDamaged]]**  |
| FOnInventorySlotsUpdated | **[[OnInventorySlotsUpdated]]**  |
| FOnItemStackChanged | **[[OnItemStackChanged]]**  |
| FOnMountingHorse | **[[OnMountingHorse]]**  |
| FOnProjectileHitPassiveShield | **[[OnProjectileHitPassiveShield]]**  |
| FOnProjectilePenetratedPassiveShield | **[[OnProjectilePenetratedPassiveShield]]**  |
| FOnProjectileStarted | **[[ProjectileStarted]]**  |
| FOnProjectileFinished | **[[ProjectileStopped]]**  |
| [FLoadout](/docs/SDK/Source/Classes/structFLoadout.md) | **[[SpawnedLoadout]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[WeaponFists]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[WeaponKnife]]**  |
| uint8 | **[[bDisableAttackInputs]]**  |
| bool | **[[bLoadoutSpawned]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [FWeaponAbilityGrant](/docs/SDK/Source/Classes/structFWeaponAbilityGrant.md) > | **[[AbilitySlots]]**  |
| [FReplicatedArray_AInventoryItemPtr](/docs/SDK/Source/Classes/structFReplicatedArray__AInventoryItemPtr.md) | **[[AmmoItems]]**  |
| float | **[[BandageRefillDisplayDuration]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[CustomizationItemToEquip]]**  |
| EWeaponAbilitySlotKey | **[[DashPressed_Ability]]**  |
| [FReplicatedArray_AInventoryItemPtr](/docs/SDK/Source/Classes/structFReplicatedArray__AInventoryItemPtr.md) | **[[DualWieldOffhandItems]]**  |
| TArray< EInventoryItemSlot > | **[[EquipPriority]]**  |
| TArray< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * > | **[[EquippedItems]]**  |
| EFaction | **[[Faction]]**  |
| TArray< EEquippedHand > | **[[HandPriority]]**  |
| EWeaponAbilitySlotKey | **[[HorseDashPressed_Ability]]**  |
| TMap< FName, EInventoryItemSlot > | **[[InventoryKeybindToSlot]]**  |
| [FReplicatedArray_AInventoryItemPtr](/docs/SDK/Source/Classes/structFReplicatedArray__AInventoryItemPtr.md) | **[[InventorySlots]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[ItemToReload]]**  |
| TArray< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * > | **[[ItemsToEquip]]**  |
| TArray< [FKeyPressedParams](/docs/SDK/Source/Classes/structFKeyPressedParams.md) > | **[[KeyPressedAbility]]**  |
| TMap< FName, EWeaponAbilitySlotKey > | **[[KeybindToSlot]]**  |
| TMap< EWeaponAbilitySlotKey, FName > | **[[Keybinds]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[KnifeClass]]**  |
| float | **[[LastTriedBandageWorldTimeSeconds]]**  |
| TArray< EInventoryItemSlot > | **[[NextPrevEquipExclusions]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[NoveltyItemClass]]**  |
| EInventoryItemSlot | **[[OffHandEquippedOnDrop]]**  |
| TArray< EInventoryItemSlot > | **[[PreviousEquippedSlots]]**  |
| EWeaponAbilitySlotKey | **[[ShovePressed_Ability]]**  |
| [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) * | **[[SpawnedLoadoutSelection]]**  |
| EKillReason | **[[SuicideReason]]**  |
| bool | **[[bIsAddingItem]]**  |
| bool | **[[bIsEquippingItem]]**  |
| bool | **[[bIsPickingUpItem]]**  |
| bool | **[[bIsReloading]]**  |
| [FReplicated_Bool](/docs/SDK/Source/Classes/structFReplicated__Bool.md) | **[[bIsUnequippingOnMount]]**  |
| bool | **[[bWantsToEquipShield]]**  |
| bool | **[[bWantsToSuicide]]**  |
| bool | **[[bWasKilled]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
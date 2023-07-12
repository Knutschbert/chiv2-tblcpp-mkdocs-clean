---
title: UAIControlHandler
type: class
aliases: UAIControlHandler
share: false

---

# UAIControlHandler





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| EWeaponAbilitySlotKey | **[[GetWeaponAbilitySlotKey]]**(const FName & Name) const |
| void | **[[Initialize]]**() |
| void | **[[OnPossess]]**(APawn * Pawn) |
| bool | **[[RequestAction]]**(EWeaponAbilitySlotKey Action, UObject * RequestedBy, EInputPriority Priority) |
| bool | **[[RequestSprint]]**(UObject * RequestedBy) |
| bool | **[[RevokeAction]]**(EWeaponAbilitySlotKey Action, UObject * RequestedBy, EInputPriority Priority) |
| void | **[[RevokeAllActionsFromObject]]**(UObject * RequestedBy) |
| bool | **[[RevokeSprint]]**(UObject * RequestedBy) |
| | **[[UAIControlHandler]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ClearActions]]**() |
| void | **[[ClearSprint]]**() |
| bool | **[[StartAction]]**(EWeaponAbilitySlotKey Action) |
| bool | **[[StopAction]]**(EWeaponAbilitySlotKey Action) |
| void | **[[UpdateAction]]**() |
| void | **[[UpdateSprint]]**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[Character]]**  |
| EWeaponAbilitySlotKey | **[[CurrentAction]]**  |
| TArray< [FInputRequest](/docs/SDK/Source/Classes/structFInputRequest.md) > | **[[InputRequestList]]**  |
| [UInventory](/docs/SDK/Source/Classes/classUInventory.md) * | **[[Inventory]]**  |
| TSet< TWeakObjectPtr< UObject > > | **[[SprintRequests]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200
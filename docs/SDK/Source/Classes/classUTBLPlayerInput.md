---
title: UTBLPlayerInput
type: class
aliases: UTBLPlayerInput
share: false

---

# UTBLPlayerInput





Inherits from UPlayerInput

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AddCompoundInputAction]]**([FTBLCompoundInputAction](/docs/SDK/Source/Classes/structFTBLCompoundInputAction.md) NewAction) |
| void | **[[ClearActionBinding]]**(FName ActionName, bool ClearMouseKeyboardBinding, bool ClearGamepadBinding) |
| void | **[[ClearAxisBinding]]**(FName AxisName, bool ClearMouseKeyboardBinding, bool ClearGamepadBinding) |
| void | **[[ClearConsoleKey]]**() |
| | **[[DECLARE_DYNAMIC_MULTICAST_DELEGATE]]**(FKeybindsReset ) |
| | **[[DECLARE_DYNAMIC_MULTICAST_DELEGATE]]**(FIsKeyInUseDialogClosed ) |
| TArray< FInputActionKeyMapping > | **[[GetAllActionKeyMappings]]**() |
| TArray< FName > | **[[GetAllActionKeyNames]]**() |
| TArray< FInputAxisKeyMapping > | **[[GetAllAxisKeyMappings]]**() |
| TArray< FName > | **[[GetAllAxisKeyNames]]**() |
| void | **[[GetDefaultKeysForAction]]**(FName ActionName, TArray< FInputActionKeyMapping > & Bindings) |
| void | **[[GetDefaultKeysForAxis]]**(FName AxisName, TArray< FInputAxisKeyMapping > & Bindings) |
| void | **[[GetKeysForAction]]**(FName ActionName, TArray< FInputActionKeyMapping > & Bindings) |
| void | **[[GetKeysForAxis]]**(FName AxisName, TArray< FInputAxisKeyMapping > & Bindings) |
| void | **[[GetKeysForConsole]]**(TArray< FKey > & ConsoleKeys) |
| void | **[[InvertGamepad]]**() |
| bool | **[[IsAltPressed]]**() |
| bool | **[[IsCtrlPressed]]**() |
| bool | **[[IsKeybindingDefault]]**(FName KeybindingName, bool ActionBinding, bool AxisBinding) |
| bool | **[[IsShiftPressed]]**() |
| void | **[[ResetActionBinding]]**(FName ActionName) |
| void | **[[ResetAllBindings]]**() |
| void | **[[ResetAxisBinding]]**(FName AxisName) |
| void | **[[ResetCompoundInputActions]]**() |
| void | **[[ResetConsoleKey]]**() |
| void | **[[SetActionBinding]]**(FName ActionName, FKey Key, bool bIsShiftPressed, bool bIsCtrlPressed, bool bIsAltPressed, bool bBypassDialog) |
| void | **[[SetAxisBinding]]**(FName AxisName, FKey Key, float Scale, bool bBypassDialog) |
| void | **[[SetConsoleKey]]**(FKey Key) |
| void | **[[SetGamepadRXSens]]**(const float Sensitivity) |
| void | **[[SetGamepadRYSens]]**(const float Sensitivity) |
| | **[[UTBLPlayerInput]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnIsKeyInUse_No]]**() |
| void | **[[OnIsKeyInUse_Yes]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [FTBLCompoundInputAction](/docs/SDK/Source/Classes/structFTBLCompoundInputAction.md) > | **[[CompoundInputActions]]**  |
| TArray< FInputActionKeyMapping > | **[[DefaultActionMappings]]**  |
| TArray< FInputAxisKeyMapping > | **[[DefaultAxisMappings]]**  |
| EInputActionMode | **[[InputActionMode]]**  |
| UDataTable * | **[[KeybindAxisDataTable]]**  |
| UDataTable * | **[[KeybindDataTable]]**  |
| FKeybindsReset | **[[KeybindsResetDelegate]]**  |
| FKeybindsReset | **[[OnIsKeyInUseDialogNoClicked]]**  |
| FKeybindsReset | **[[OnIsKeyInUseDialogYesClicked]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200
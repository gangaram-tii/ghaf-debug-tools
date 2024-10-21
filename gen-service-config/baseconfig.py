baseConfig = {
    "PrivateNetwork" : ["true", "false"],
    "IPAccounting" : ["true", "false"],

    "IPAddressDeny" : ["any", "[]"],
    "ProtectHome" : ["true", "read-only", "tmpfs", "false"],
    "ProtectSystem" :["strict", "full", "true", "false"],
    "ProtectProc" : ["noaccess", "invisible", "ptraceable", "default"],
    "PrivateTmp" : ["true", "false"],

    "PrivateMounts" : ["true", "false"],

    "ProcSubset" : ["pid","all"],

    "PrivateUsers" : ["true", "false"],
    "DynamicUser" : ["true", "false"],

  "PrivateDevices" : ["true", "false"],

  "ProtectKernelTunables" : ["true", "false"],
  "ProtectKernelModules" : ["true", "false"],
  "ProtectKernelLogs" : ["true", "false"],


  "Delegate" : ["false", "true"],
  "KeyringMode" : ["private", "inherit", "shared"],
  "NoNewPrivileges" : ["true", "false"],

  "UMask":["065", "066", "077"],
  "ProtectHostname" : ["true", "false"],
  "ProtectClock" : ["true", "false"],
  "ProtectControlGroups" : ["true", "false"],


  "LockPersonality" : ["true", "false"],
  "MemoryDenyWriteExecute" : ["true", "false"],
  "RestrictRealtime" : ["true", "false"],
  "RestrictSUIDSGID" : ["true", "false"],
  "RemoveIPC" : ["true", "false"],
  "SystemCallArchitectures" : ["native", ""],
  "NotifyAccess" : ["true", "false"],
}

{
    "PrivateNetwork" = ["true", "false"],
    "IPAccounting" = ["true", "false"],

    "IPAddressDeny" = ["any", "[]"],
    ####"RestrictAddressFamilies" = ["AF_PACKET", "AF_NETLINK", "AF_UNIX", "AF_INET", "AF_INET6"],
    "ProtectHome" = ["true", "read-only", "tmpfs", "false"],
    "ProtectSystem" =["strict", "full", "true", "false"],
    "ProtectProc" = ["noaccess", "invisible", "ptraceable", "default"],
    ###"ReadWritePaths" = ["", "/var", "/run"],
    ###"ReadOnlyPaths" = ["/etc", "/boot"],
    "PrivateTmp" = ["true", "false"],

    "PrivateMounts" = ["true", "false"],

    "ProcSubset" = ["pid","all"],

    "PrivateUsers" = ["true", "false"],
    "DynamicUser" = ["true", "false"],

  "PrivateDevices" = ["true", "false"],
  #####"DeviceAllow" =/dev/null

  "ProtectKernelTunables" = ["true", "false"],
  "ProtectKernelModules" = ["true", "false"],
  "ProtectKernelLogs" = ["true", "false"],


  "Delegate" = ["false", "true"],
  "KeyringMode" = ["private", "inherit", "shared"],
  "NoNewPrivileges" = ["true", "false"],

  "UMask"=["065", "066", "077"],
  "ProtectHostname" = ["true", "false"],
  "ProtectClock" = ["true", "false"],
  "ProtectControlGroups" = ["true", "false"],
  
  ###: RestrictNamespaces" = ["user", "pid", "net", "uts", "mnt", "cgroup", "ipc"],
  
  "LockPersonality" = ["true", "false"],
  "MemoryDenyWriteExecute" = ["true", "false"],
  "RestrictRealtime" = ["true", "false"],
  "RestrictSUIDSGID" = ["true", "false"],
  "RemoveIPC" = ["true", "false"],
  "SystemCallArchitectures" = ["native", ""],
  "NotifyAccess" = ["true", "false"],

  CapabilityBoundingSet = [
      "CAP_SYS_PACCT"
    , "CAP_KILL"
    , "CAP_WAKE_ALARM"
    , "CAP_DAC_OVERRIDE"
	, "CAP_DAC_READ_SEARCH"
    , "CAP_FOWNER"
    , "CAP_IPC_OWNER"
    , "CAP_BPF"
    , "CAP_LINUX_IMMUTABLE"
    , "CAP_IPC_LOCK"
    , "CAP_SYS_MODULE"
    , "CAP_SYS_TTY_CONFIG"
    , "CAP_SYS_BOOT"
    , "CAP_SYS_CHROOT"
    , "CAP_BLOCK_SUSPEND"
    , "CAP_LEASE"
    , "CAP_MKNOD"
    , "CAP_CHOWN"
    , "CAP_FSETID"
    , "CAP_SETFCAP"
    , "CAP_SETUID"
    , "CAP_SETGID"
    , "CAP_SETPCAP"
    , "CAP_MAC_ADMIN"
    , "CAP_MAC_OVERRIDE"
    , "CAP_SYS_RAWIO"
    , "CAP_SYS_PTRACE"
    , "CAP_SYS_NICE"
    , "CAP_SYS_RESOURCE"
    , "CAP_NET_ADMIN"
    , "CAP_NET_BIND_SERVICE"
    , "CAP_NET_BROADCAST"
    , "CAP_NET_RAW"
    , "CAP_AUDIT_CONTROL"
    , "CAP_AUDIT_READ"
    , "CAP_AUDIT_WRITE"
    , "CAP_SYS_ADMIN"
    , "CAP_SYSLOG"
    , "CAP_SYS_TIME
  ],

AmbientCapabilities=[
      "CAP_SYS_PACCT"
    , "CAP_KILL"
    , "CAP_WAKE_ALARM"
    , "CAP_DAC_OVERRIDE"
	, "CAP_DAC_READ_SEARCH"
    , "CAP_FOWNER"
    , "CAP_IPC_OWNER"
    , "CAP_BPF"
    , "CAP_LINUX_IMMUTABLE"
    , "CAP_IPC_LOCK"
    , "CAP_SYS_MODULE"
    , "CAP_SYS_TTY_CONFIG"
    , "CAP_SYS_BOOT"
    , "CAP_SYS_CHROOT"
    , "CAP_BLOCK_SUSPEND"
    , "CAP_LEASE"
    , "CAP_MKNOD"
    , "CAP_CHOWN"
    , "CAP_FSETID"
    , "CAP_SETFCAP"
    , "CAP_SETUID"
    , "CAP_SETGID"
    , "CAP_SETPCAP"
    , "CAP_MAC_ADMIN"
    , "CAP_MAC_OVERRIDE"
    , "CAP_SYS_RAWIO"
    , "CAP_SYS_PTRACE"
    , "CAP_SYS_NICE"
    , "CAP_SYS_RESOURCE"
    , "CAP_NET_ADMIN"
    , "CAP_NET_BIND_SERVICE"
    , "CAP_NET_BROADCAST"
    , "CAP_NET_RAW"
    , "CAP_AUDIT_CONTROL"
    , "CAP_AUDIT_READ"
    , "CAP_AUDIT_WRITE"
    , "CAP_SYS_ADMIN"
    , "CAP_SYSLOG"
    , "CAP_SYS_TIME
  ],
  
SystemCallFilter = [
     "@aio",
     "@basic-io",
     "@chown",
     "@clock",
     "@cpu-emulation",
     "@debug",
     "@file-system",
     "@io-event",
     "@ipc",
     "@keyring",
     "@memlock",
     "@module",
     "@mount",
     "@network-io",
     "@obsolete",
     "@pkey",
     "@privileged",
     "@process",
     "@raw-io",
     "@reboot",
     "@resources",
     "@sandbox",
     "@setuid",
     "@signal",
     "@swap",
     "@sync",
     "@system-service",
     "@timer",
     "@known",
  ],
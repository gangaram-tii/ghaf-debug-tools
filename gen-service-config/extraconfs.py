extraconfs = {
    "RestrictAddressFamilies" : ["AF_PACKET", "AF_NETLINK", "AF_UNIX", "AF_INET", "AF_INET6"],
    "RestrictNamespaces" : ["user", "pid", "net", "uts", "mnt", "cgroup", "ipc"]
}
#"ReadWritePaths" : ["", "/var", "/run"],
#"ReadOnlyPaths" : ["/etc", "/boot"],
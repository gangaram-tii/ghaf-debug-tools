{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.iperf3
    pkgs.gcc
    pkgs.python311Full
    pkgs.python311Packages.scp
    pkgs.python311Packages.matplotlib
    pkgs.python311Packages.virtualenv
  ];

  shellHook = ''
    if [ ! -d .venv ]; then
      virtualenv .venv
      source .venv/bin/activate
      pip install paramiko
    else
      source .venv/bin/activate
    fi
    echo "Welcome to your Python development environment."
  '';
}


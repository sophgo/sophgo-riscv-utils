# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This directory provides a way to run Broadcom's `storcli64` (RAID/storage controller management CLI) on a RISC-V host (Sophgo SG2260 platform). Since storcli64 is an x86-64 binary and the SG2260 is a RISC-V system, it uses QEMU user-mode emulation (`qemu-x86_64`, built for RISC-V) to bridge the architecture gap.

## Binaries

- **`storcli64`** — Broadcom StorCLI utility v007.1804.0000.0000 (Apr 2021). ELF 64-bit x86-64, statically linked. Manages MegaRAID/SAS controllers: create/delete VDs, show controller/enclosure/disk status, firmware updates, BBU/CacheVault management, etc.
- **`qemu-x86_64`** — QEMU user-mode emulator for x86-64 on RISC-V. ELF 64-bit RISC-V, statically linked. Translates x86-64 syscalls to the host RISC-V kernel so x86-64 binaries run without a full VM.

## Running storcli64

```bash
./qemu-x86_64 ./storcli64 <storcli_command>
```

Common commands:
- `./qemu-x86_64 ./storcli64 show` — list controllers
- `./qemu-x86_64 ./storcli64 /c0 show` — show controller 0 details
- `./qemu-x86_64 ./storcli64 /c0/eall/sall show` — show all physical drives
- `./qemu-x86_64 ./storcli64 /c0/vall show` — show all virtual drives
- `./qemu-x86_64 ./storcli64 help` — full command reference

## Architecture Context

The host system is aarch64 (ARM64) running Linux 6.2. The SG2260 Sophgo RISC-V board would be the target deployment — the qemu binary here is a RISC-V executable specifically for that platform. On the current aarch64 host, the RISC-V qemu itself cannot run directly without its own emulation layer. This setup is designed for deployment on the actual SG2260 RISC-V hardware where `qemu-x86_64` runs natively and then emulates x86-64 for storcli64.
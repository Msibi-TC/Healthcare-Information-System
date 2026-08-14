"""Healthcare Information System backend package.

Domain models are intentionally not imported here. Several models are not yet
implemented, and importing incomplete persistence code during package startup
would prevent independent components such as the health endpoint from loading.
Model registration will be introduced explicitly when the persistence layer is
ready for migrations.
"""

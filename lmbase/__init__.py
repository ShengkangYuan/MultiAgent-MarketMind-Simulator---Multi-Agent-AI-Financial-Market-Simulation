"""Mock lmbase package for offline operation.

Provides minimal implementations of BlockBasedStoreManager, InferInput,
InferOutput, and LangChainAPIInference so that masim can run without
the real lmbase package installed.
"""

__version__ = "0.0.1-mock"

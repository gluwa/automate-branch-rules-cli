"""Change the config values."""
branches = ('main',)  # Note: Single element requires a comma at end.
add_codeowners_file = False
signed_commit = False
branch_rules = {"required_approving_review_count": 1,
                "require_code_owner_reviews": True,
                "contexts": ["CodeQL"],
                "strict": True
                }

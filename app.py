                    toggle_prompt = st.checkbox(
                        f"Automatically generate system prompt for Metric {i + 1}", key=f"toggle_prompt_{i}"
                    )

                    if toggle_prompt:
                        # Use hardcoded system prompt "huhu" when the checkbox is selected
                        system_prompt = "huhu"
                        st.text_area(
                            f"Generated System Prompt for Metric {i + 1}:", value=system_prompt, height=200
                        )
                        st.success(f"System Prompt for Metric {i + 1} is hardcoded as 'huhu'.")
                    else:
                        system_prompt = st.text_area(
                            f"Enter the System Prompt for Metric {i + 1}:",
                            height=200
                        )

                        valid_prompt = st.button(f"Validate Metric {i + 1}", key=f"validate_{i}")

                        if valid_prompt:
                            selected_column_terms = {
                                col.lower().replace(" ", "_"): col
                                for col in selected_columns
                            }
                            errors = []
                            for term, original_column in selected_column_terms.items():
                                term_pattern = f"\\b{term.replace('_', ' ')}\\b"
                                if not re.search(term_pattern, system_prompt, re.IGNORECASE):
                                    errors.append(f"'{original_column}' needs to be included as '{term.replace('_', ' ')}' in the system prompt.")

                            if errors:
                                st.error(
                                    f"For Metric {i + 1}, the following errors were found in your system prompt: "
                                    f"{'; '.join(errors)}"
                                )
                            else:
                                st.success(f"System Prompt for Metric {i + 1} is valid.")

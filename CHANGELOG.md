## v1.8.20 - 2024-12-14
## v1.8.20

### Internal Changes
- Enhanced the changelog generation script to include mermaid diagrams for visual representation of changes.
- Increased the `max_tokens` parameter for OpenAI API calls from 500 to 750 to allow for more detailed changelog entries.

### Mermaid Diagram Representation

```mermaid
graph TD;
    A[Changelog Generation Script] -->|Updated| B[Include Mermaid Diagrams];
    A -->|Increased| C[Max Tokens for API Calls];
```

These changes improve the clarity and detail of the changelog entries, providing better insights into updates and modifications.

## v1.8.19 - 2024-12-14
## v1.8.19

### Internal Changes
- Updated the dependabot configuration to check for updates daily instead of weekly.
- Modified the GitHub Actions workflow to exclude dependabot from triggering certain steps, ensuring that version increments and changelog updates are only performed by human contributors.

## v1.8.17 - 2024-12-14
## v1.8.17

### Internal Changes

- Updated the version number to 1.8.17 in the `__version__.py` file.
- Changed the Dependabot update schedule from daily to weekly in `.github/dependabot.yml` for better management of dependency updates.

## v1.8.16 - 2024-12-14
## v1.8.16

### Internal Changes

- Updated the `generate_changelog.py` script to remove backticks from the generated changelog entry, ensuring cleaner formatting.
- Bumped the version number to 1.8.16 in the `__version__.py` file.

## v1.8.15 - 2024-12-14
```markdown
## v1.8.15

### Internal Changes

- Improved the GitHub Actions workflow for version increments:
  - The changelog entry is now written to a temporary file before being appended to the existing `CHANGELOG.md`, ensuring a cleaner update process.
  - Enhanced the method for setting the output of the changelog entry in the workflow, replacing the deprecated `set-output` command with a more robust approach.
- Updated the `generate_changelog.py` script to ensure the changelog entry generation process adheres to the latest guidelines, specifically excluding dates and release status from entries.
```

## v1.8.14 - 2024-12-14
## v1.8.14

### Internal Changes

- Improved the GitHub Actions workflow for version increments:
  - The changelog entry is now written to a temporary file before being appended to the existing `CHANGELOG.md`, ensuring a cleaner update process.
  - Enhanced the method for setting the output of the changelog entry in the workflow, replacing the deprecated `set-output` command with a more robust approach.
- Updated the `generate_changelog.py` script to ensure the changelog entry generation process adheres to the latest guidelines, specifically excluding dates and release status from entries.

## v1.8.12 - 2024-12-14
# Changelog

## v1.8.12

### Internal Changes

- Updated the version increment workflow to simplify the condition for updating `CHANGELOG.md`. The check for non-empty `diff` output has been removed, and now it only checks if `env.new_version` is not empty. This change streamlines the workflow process for updating the changelog.

## v1.8.13 - 2024-12-14
# Changelog

## v1.8.13 - 2023-10-XX

### Internal Changes

- Enhanced the GitHub Actions workflow for version increments. The process now includes reading the changelog entry from a file and using it as the body of the release notes. This improvement ensures that the release notes are automatically populated with the latest changelog entry.
- Re-enabled the steps for creating a new GitHub release and triggering the release workflow. The workflow now checks if `env.new_version` is not empty before proceeding, improving the automation of the release process.
# Changelog

## v1.8.0

### New Features
- **Fulfillment Inbound API**: Added `list_shipment_boxes` method to provide a paginated list of box packages in a shipment.
- **Fulfillment Inbound API**: Added `update_shipment_tracking_details` method to update a shipment's tracking details.
- **Marketplaces**: Added support for the Amazon marketplace in Ireland (IE).

### Dependency Updates
- Updated `boto3` dependency from `~=1.35.67` to `~=1.35.80`.

### Internal Changes
- Updated the `setup.cfg` to include the `name` field for the package metadata.
- Modified the GitHub Actions workflow to ensure `setuptools`, `wheel`, and `twine` are upgraded during the installation process.

# Changelog

## v1.6.1 - v1.7.1

### New Features
- **Amazon Warehousing and Distribution (AWD) API**: Added new endpoint `AmazonWarehousingAndDistribution` with versioning support.
- **Shipping V2 API**: Introduced a new `Shipping` API client with multiple endpoints including `get_rates`, `purchase_shipment`, `one_click_shipment`, `get_tracking`, `cancel_shipment`, `get_access_points`, `submit_ndr_feedback`, and more.
- **Listings Items API**: Added `search_listings_items` endpoint to search and return a list of listings items and their details.
- **Sellers API**: Added `get_account` endpoint to retrieve seller account information and associated marketplaces.
- **Fulfillment Inbound API**: Added multiple new endpoints for managing inbound plans, shipments, and delivery windows.
- **Reports API**: Enhanced iterable handling for `reportTypes`, `processingStatuses`, and `marketplaceIds` parameters to exclude strings.

### Enhancements
- **Versioning Support**: Introduced versioning for clients with multiple versions, allowing users to specify the version when constructing a new client.
- **Documentation**: Updated and expanded documentation, including new sections for versioning and endpoints.
- **Security**: Added a `SECURITY.md` file outlining the security policy and vulnerability reporting process.
- **README**: Enhanced with new badges, support options, and improved documentation links.

### Bug Fixes
- **Inventories API**: Fixed an issue with `sellerSkus` parameter to ensure it is properly handled as an iterable, excluding strings.
- **Listings Items API**: Corrected handling of `includedData` parameter to ensure it is properly processed as an iterable, excluding strings.
- **Reports API**: Fixed iterable handling for parameters to ensure proper processing when not a string.

### Internal Changes
- **CI/CD**: Added a new GitHub Actions workflow for version incrementing and release creation.
- **Dependencies**: Updated dependencies in `requirements.txt` and `docs/requirements.txt` to newer versions.
- **Code Quality**: Removed SonarCloud configuration file and associated badges from the README.
- **Testing**: Added new tests for `Shipping V2` and `Listings Items` APIs to ensure functionality and reliability.

This release introduces significant new features, enhancements, and bug fixes to improve the functionality and usability of the `python-amazon-sp-api` library.

# Changelog

## v1.6.0

### New Features
- **Amazon Warehousing and Distribution API**: Added a new client for the Amazon Warehousing and Distribution (AWD) API. This includes endpoints for:
  - Retrieving an AWD inbound shipment.
  - Listing inbound AWD shipments with optional filters.
  - Listing AWD inventory with optional filters.

### Changes
- **Data Kiosk API**: Updated the request handling to include `add_marketplace=False` for several endpoints, ensuring marketplace information is not added to these requests.
- **Feeds API**: Improved the `get_feed_result_document` method to clarify that it fetches the feed result document's contents by first retrieving from the `getFeedDocument` endpoint and then fetching from the returned URL. Updated the return type to `str`.

### Bug Fixes
- **Access Token Response**: Corrected the `expires_in` attribute to correctly retrieve the expiration time from the response.
- **ApiResponse**: Enhanced the `next_token` property to also check for `nextPageToken` in the response payload.

### Internal
- **Dependencies**: Updated `requests` to version `2.32.3` and `boto3` to version `1.34.144` in both `requirements.txt` and `docs/requirements.txt`.
- **Client Initialization**: Added a donation message during client initialization to encourage support for the project. This message can be disabled by setting the `ENV_DISABLE_DONATION_MSG=1` environment variable.

# Changelog

## [v1.5.0]

### New Features
- **FulfillmentInbound API**: Added support for the new FulfillmentInbound API version `2024-03-20`, including:
  - `list_inbound_plans`
  - `create_inbound_plan`
  - `get_inbound_plan`
  - `list_inbound_plan_boxes`
  - `cancel_inbound_plan`
  - `list_inbound_plan_items`
  - `set_packing_information`
  - `list_packing_options`
  - `generate_packing_options`
  - `confirm_packing_option`
  - `list_packing_group_items`
  - `list_inbound_plan_pallets`
  - `list_placement_options`
  - `generate_placement_options`
  - `confirm_placement_option`
  - `get_shipment`
  - `get_delivery_challan_document`
  - `update_shipment_delivery_window`
  - `get_self_ship_appointment_slots`
  - `generate_self_ship_appointment_slots`
  - `cancel_self_ship_appointment`
  - `schedule_self_ship_appointment`
  - `update_shipment_tracking_details`
  - `list_transportation_options`
  - `generate_transportation_options`
  - `confirm_transportation_options`
  - `list_item_compliance_details`
  - `update_item_compliance_details`
  - `get_inbound_operation_status`

### Changes
- **Catalog API**: Reduced the burst rate limit from 40 to 2 requests per second.
- **Feeds API**: Fixed encoding issue by changing `upload_data.decode('iso-8859-1')` to `upload_data.encode('iso-8859-1')`.

### Bug Fixes
- **DataKiosk API**: Improved file handling in `_handle_file` method to correctly handle both bytes and string documents.

### Dependencies
- Updated `boto3` from `1.34.2` to `1.34.87`.
- Updated `cachetools` from `5.3.2` to `5.3.3`.

# Changelog

## v1.4.0

### New Features
- **Application Management API**: Added a new client for the Application Management API, allowing developers to programmatically update the client secret on registered applications. This includes the `rotate_application_client_secret` method to rotate application client secrets.
- **Enums Documentation**: Introduced documentation for various enums used within the API, such as `Marketplaces`, `FeedTypes`, `FulfillmentChannels`, and more.

### Changes
- **Listings Items API**: Updated the `get_listings_item` method to handle `includedData` as an iterable, converting it to a comma-separated string if necessary.
- **Documentation Updates**: 
  - Removed consultation and playground sections from the README.
  - Removed API documentation buttons from various endpoint documentation pages.
  - Added `enums` section to the documentation index for better visibility of available enums.
- **Dependencies**: Updated `boto3` dependency from `1.29.3` to `1.34.2`.

### Internal Changes
- **Code Cleanup**: Commented out unused sections in the documentation footer and layout templates.
- **Enum Enhancements**: Improved enum classes by adding string inheritance and documentation comments for better clarity and usage.
- **Documentation Build**: Added new Sphinx extensions to support enum documentation and compatibility.

These changes enhance the functionality and usability of the `python-amazon-sp-api` package, providing developers with more tools and clearer documentation for integrating with Amazon's Selling Partner API.

# Changelog

## v1.3.0

### New Features
- **Data Kiosk API Support**: Added support for the Data Kiosk API, allowing users to create and manage queries for sales and traffic analytics. Introduced the `DataKiosk` client with methods such as `create_query`, `get_document`, and others for interacting with the Data Kiosk API.
- **New Endpoints**: Added new endpoints for `data_kiosk`, `replenishment`, and `supply_sources` in the documentation.
- **AWS Secret Manager Authentication**: Introduced optional installation for AWS Secret Manager Authentication with `pip install "python-amazon-sp-api[aws]"` and caching support with `pip install "python-amazon-sp-api[aws-caching]"`.

### Changes
- **Dependencies**: Updated `boto3` dependency from `~=1.29.2` to `~=1.29.3`.
- **Rate Limit Documentation**: Improved the documentation format for rate limits in the Data Kiosk API to use tables for better readability.

### Notifications
- **New Notification Type**: Added `DATA_KIOSK_QUERY_PROCESSING_FINISHED` notification type to notify when a Data Kiosk query finishes processing.

# Changelog

## v1.2.0

### New Features
- **Data Kiosk API**: Introduced a new `data_kiosk` module to interact with Amazon's Data Kiosk API.
  - Added `get_document` method with enhanced functionality:
    - Supports downloading documents directly by setting the `download` parameter to `True`.
    - Allows writing the document to a specified file using the `file` parameter, which accepts `BytesIO`, `StringIO`, `BinaryIO`, or `TextIO`.
    - Added support for specifying file encoding via the `encoding` parameter, defaulting to `utf-8`.

- **New APIs**: Added new modules for:
  - `replenishment`
  - `supply_sources`

### Internal Changes
- Updated project version from `1.1.0` to `1.2.0`.

# Changelog

## v1.0.0

### Breaking Changes
- **Authentication Update**: Removed AWS IAM or AWS Signature Version 4 authentication. The library no longer requires AWS credentials for standard operations. AWS credentials can still be passed but will be ignored unless using SecretsManager Auth.

### Enhancements
- **Datetime Handling**: Improved the datetime formatting in the `Sales` API to use `isoformat` with timezone awareness, ensuring consistent and accurate timestamp representation.

### Dependency Updates
- Updated `boto3` to version `1.28.63`.
- Updated `setuptools` to version `68.2.2`.

### Internal Changes
- Removed the `aws_sig_v4.py` module, along with related AWS signature authentication logic from the `client.py` file.
- Added `.readthedocs.yaml` configuration file to support building documentation with Read the Docs.

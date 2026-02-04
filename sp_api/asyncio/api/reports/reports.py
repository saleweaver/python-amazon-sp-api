from datetime import datetime
from typing import Optional, Union

from sp_api.base import (
    Client,
    sp_endpoint,
    fill_query_params,
    ApiResponse,
    Marketplaces,
)
from sp_api.asyncio.base import AsyncBaseClient
from sp_api.util import (
    normalize_csv_param,
    normalize_datetime_kwargs,
    normalize_marketplace_ids,
    should_add_marketplace,
)
from sp_api.util.report_document import (
    decode_document,
    decompress_bytes,
    handle_file,
    resolve_character_code,
    stream_to_file_async,
)


class Reports(AsyncBaseClient):
    """
    Reports SP-API Client
    :link:

    The Selling Partner API for Reports lets you retrieve and manage a variety of reports that can help selling partners manage their businesses.
    """

    @sp_endpoint("/reports/2021-06-30/reports", method="GET")
    async def get_reports(self, **kwargs) -> ApiResponse:
        """
        get_reports(self, **kwargs) -> ApiResponse
        
        Returns report details for the reports that match the filters that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Reports().get_reports()
        
        Args:
            key reportTypes: object |  A list of report types used to filter reports. Refer to [Report Type Values](https://developer-docs.amazon.com/sp-api/docs/report-type-values) for more information. When reportTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either reportTypes or nextToken is required.
            key processingStatuses: object |  A list of processing statuses used to filter reports.
            key marketplaceIds: object |  A list of marketplace identifiers used to filter reports. The reports returned will match at least one of the marketplaces that you specify.
            key pageSize: object |  The maximum number of reports to return in a single call.
            key createdSince: object |  The earliest report creation date and time for reports to include in the response, in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date time format. The default is 90 days ago. Reports are retained for a maximum of 90 days.
            key createdUntil: object |  The latest report creation date and time for reports to include in the response, in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date time format. The default is now.
            key nextToken: object |  A string token returned in the response to your previous request. `nextToken` is returned when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the `getReports` operation and include this token as the only parameter. Specifying `nextToken` with any other parameters will cause the request to fail.
        
        Returns:
            ApiResponse
        """
        normalize_csv_param(kwargs, "reportTypes")
        normalize_csv_param(kwargs, "processingStatuses")
        normalize_marketplace_ids(kwargs, marketplace_cls=Marketplaces)
        normalize_datetime_kwargs(kwargs, ["createdSince", "createdUntil"])
        add_marketplace = should_add_marketplace(kwargs, "nextToken")
        return await self._request(
            kwargs.pop("path"),
            params=kwargs,
            add_marketplace=add_marketplace,
        )

    @sp_endpoint("/reports/2021-06-30/reports", method="POST")
    async def create_report(self, **kwargs) -> ApiResponse:
        """
        create_report(self, **kwargs) -> ApiResponse
        
        Creates a report.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0167                                  15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Reports().create_report()
        
        Args:
            body: CreateReportSpecification | required Information required to create the report.
        
        Returns:
            ApiResponse
        """
        normalize_datetime_kwargs(kwargs, ["dataStartTime", "dataEndTime"])
        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/reports/2021-06-30/reports/{}", method="DELETE")
    async def cancel_report(self, reportId, **kwargs) -> ApiResponse:
        """
        cancel_report(self, reportId, **kwargs) -> ApiResponse
        
        Cancels the report that you specify. Only reports with `processingStatus=IN_QUEUE` can be cancelled. Cancelled reports are returned in subsequent calls to the `getReport` and `getReports` operations.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Reports().cancel_report("value")
        
        Args:
            reportId: object | required The identifier for the report. This identifier is unique only in combination with a seller ID.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), reportId), data=kwargs
        )

    @sp_endpoint("/reports/2021-06-30/reports/{}", method="GET")
    async def get_report(self, reportId, **kwargs) -> ApiResponse:
        """
        get_report(self, reportId, **kwargs) -> ApiResponse
        
        Returns report details (including the `reportDocumentId`, if available) for the report that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Reports().get_report("value")
        
        Args:
            reportId: object | required The identifier for the report. This identifier is unique only in combination with a seller ID.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), reportId), params=kwargs
        )

    @sp_endpoint("/reports/2021-06-30/schedules", method="GET")
    async def get_report_schedules(self, **kwargs) -> ApiResponse:
        """
        get_report_schedules(self, **kwargs) -> ApiResponse
        
        Returns report schedule details that match the filters that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Reports().get_report_schedules()
        
        Args:
            key reportTypes: object | required A list of report types used to filter report schedules. Refer to [Report Type Values](https://developer-docs.amazon.com/sp-api/docs/report-type-values) for more information.
        
        Returns:
            ApiResponse
        """
        normalize_csv_param(kwargs, "reportTypes")

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/reports/2021-06-30/schedules", method="POST")
    async def create_report_schedule(self, **kwargs) -> ApiResponse:
        """
        create_report_schedule(self, **kwargs) -> ApiResponse
        
        Creates a report schedule. If a report schedule with the same report type and marketplace IDs already exists, it will be cancelled and replaced with this one.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Reports().create_report_schedule()
        
        Args:
            body: CreateReportScheduleSpecification | required Information required to create the report schedule.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/reports/2021-06-30/schedules/{}", method="DELETE")
    async def cancel_report_schedule(self, reportScheduleId, **kwargs) -> ApiResponse:
        """
        cancel_report_schedule(self, reportScheduleId, **kwargs) -> ApiResponse
        
        Cancels the report schedule that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Reports().cancel_report_schedule("value")
        
        Args:
            reportScheduleId: object | required The identifier for the report schedule. This identifier is unique only in combination with a seller ID.
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), reportScheduleId), data=kwargs
        )

    def delete_report_schedule(self, reportScheduleId, **kwargs) -> ApiResponse:
        """
        delete_report_schedule(self, reportScheduleId, **kwargs) -> ApiResponse
        
        cancel_report_schedule(self, reportScheduleId, **kwargs) -> ApiResponse
                                Cancels the report schedule that you specify.
        
        Examples:
            literal blocks::
            
                Reports().delete_report_schedule("value")
        
        Args:
            reportScheduleId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return self.cancel_report_schedule(reportScheduleId)

    @sp_endpoint("/reports/2021-06-30/schedules/{}", method="GET")
    async def get_report_schedule(self, reportScheduleId, **kwargs) -> ApiResponse:
        """
        get_report_schedule(self, reportScheduleId, **kwargs) -> ApiResponse
        
        Returns report schedule details for the report schedule that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Reports().get_report_schedule("value")
        
        Args:
            reportScheduleId: object | required The identifier for the report schedule. This identifier is unique only in combination with a seller ID.
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), reportScheduleId), params=kwargs
        )

    @sp_endpoint("/reports/2021-06-30/documents/{}", method="GET")
    async def get_report_document(
        self,
        reportDocumentId,
        download: bool = False,
        file=None,
        character_code: Optional[str] = None,
        stream: bool = False,
        timeout: Optional[Union[float,int]] = None,
        **kwargs
    ) -> ApiResponse:
        """
        get_report_document(self, reportDocumentId, download, file, character_code, stream, timeout, **kwargs) -> ApiResponse
        
        Returns the information required for retrieving a report document's contents.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0167                                  15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Reports().get_report_document("value", "value", "value", "value", "value", "value")
        
        Args:
            reportDocumentId: object | required The identifier for the report document.
        
        Returns:
            ApiResponse
        """
        res = await self._request(
            fill_query_params(kwargs.pop("path"), reportDocumentId),
            add_marketplace=False,
        )
        if download or file or ("decrypt" in kwargs and kwargs["decrypt"]):
            compression_algorithm = res.payload.get("compressionAlgorithm")
            if stream and file:
                async with self._transport.stream(
                    "GET",
                    res.payload.get("url"),
                    timeout=timeout,
                ) as document_response:
                    if not character_code:
                        character_code = resolve_character_code(
                            document_response.encoding, fallback="iso-8859-1"
                        )
                    await stream_to_file_async(
                        document_response,
                        file,
                        character_code,
                        compression_algorithm,
                    )
            else:
                document_response = await self._transport.request(
                    "GET",
                    res.payload.get("url"),
                    timeout=timeout,
                )
                if not character_code:
                    character_code = resolve_character_code(
                        document_response.encoding, fallback="iso-8859-1"
                    )
                document = decompress_bytes(
                    document_response.content, compression_algorithm
                )
                decoded_document = decode_document(document, character_code)
                if download:
                    res.payload.update(
                        {
                            "document": decoded_document,
                        }
                    )
                if file:
                    handle_file(file, decoded_document, character_code)
        return res

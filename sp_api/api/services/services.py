import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Services(Client):
    """
    Services SP-API Client
    :link:

    With the Services API, you can build applications that help service providers get and modify their service orders.
    """

    @sp_endpoint("/service/v1/serviceJobs/{}", method="GET")
    def get_service_job_by_service_job_id(self, serviceJobId, **kwargs) -> ApiResponse:
        """
        get_service_job_by_service_job_id(self, serviceJobId, **kwargs) -> ApiResponse

        Gets service job details for the service job indicated by the service job identifier you specify.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        20                                      40
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            serviceJobId:string | * REQUIRED A service job identifier.

        Returns:
            ApiResponse:
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), serviceJobId), params=kwargs
        )

    @sp_endpoint("/service/v1/serviceJobs/{}/cancellations", method="PUT")
    def cancel_service_job_by_service_job_id(
        self, serviceJobId, **kwargs
    ) -> ApiResponse:
        """
        cancel_service_job_by_service_job_id(self, serviceJobId, **kwargs) -> ApiResponse

        Cancels the service job indicated by the service job identifier you specify.

        **Usage Plan:**


        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            serviceJobId:string | * REQUIRED An Amazon defined service job identifier.
            key cancellationReasonCode:string | * REQUIRED A cancel reason code that specifies the reason for cancelling a service job.

        Returns:
            ApiResponse:
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), serviceJobId), data=kwargs
        )

    @sp_endpoint("/service/v1/serviceJobs/{}/completions", method="PUT")
    def complete_service_job_by_service_job_id(
        self, serviceJobId, **kwargs
    ) -> ApiResponse:
        """
        complete_service_job_by_service_job_id(self, serviceJobId, **kwargs) -> ApiResponse

        Completes the service job indicated by the service job identifier you specify.

        **Usage Plan:**


        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            serviceJobId:string | * REQUIRED An Amazon defined service job identifier.

        Returns:
            ApiResponse:
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), serviceJobId), data=kwargs
        )

    @sp_endpoint("/service/v1/serviceJobs", method="GET")
    def get_service_jobs(self, **kwargs) -> ApiResponse:
        """
        get_service_jobs(self, **kwargs) -> ApiResponse

        Gets service job details for the specified filter query.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      40
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            key serviceOrderIds: array |  List of service order ids for the query you want to perform.Max values supported 20.
            key serviceJobStatus: array |  A list of one or more job status by which to filter the list of jobs.
            key pageToken: string |  String returned in the response of your previous request.
            key pageSize: integer |  A non-negative integer that indicates the maximum number of jobs to return in the list, Value must be 1 - 20. Default 20.
            key sortField: string |  Sort fields on which you want to sort the output.
            key sortOrder: string |  Sort order for the query you want to perform.
            key createdAfter: string |  A date used for selecting jobs created after (or at) a specified time must be in ISO 8601 format. Required if LastUpdatedAfter is not specified.Specifying both CreatedAfter and LastUpdatedAfter returns an error.
            key createdBefore: string |  A date used for selecting jobs created before (or at) a specified time must be in ISO 8601 format.
            key lastUpdatedAfter: string |  A date used for selecting jobs updated after (or at) a specified time must be in ISO 8601 format. Required if createdAfter is not specified.Specifying both CreatedAfter and LastUpdatedAfter returns an error.
            key lastUpdatedBefore: string |  A date used for selecting jobs updated before (or at) a specified time must be in ISO 8601 format.
            key scheduleStartDate: string |  A date used for filtering jobs schedule after (or at) a specified time must be in ISO 8601 format. schedule end date should not be earlier than schedule start date.
            key scheduleEndDate: string |  A date used for filtering jobs schedule before (or at) a specified time must be in ISO 8601 format. schedule end date should not be earlier than schedule start date.
            key marketplaceIds: array | * REQUIRED Used to select jobs that were placed in the specified marketplaces.

        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/service/v1/serviceJobs/{}/appointments", method="POST")
    def add_appointment_for_service_job_by_service_job_id(
        self, serviceJobId, **kwargs
    ) -> ApiResponse:
        """
        add_appointment_for_service_job_by_service_job_id(self, serviceJobId, **kwargs) -> ApiResponse

        Adds an appointment to the service job indicated by the service job identifier you specify.

        **Usage Plan:**


        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            serviceJobId:string | * REQUIRED An Amazon defined service job identifier.
            body: {
              "appointmentTime": {
                "startTime": "2019-08-24T14:15:22Z",
                "durationInMinutes": 0
              }
            }

         Returns:
            ApiResponse:
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), serviceJobId), data=kwargs
        )

    @sp_endpoint("/service/v1/serviceJobs/{}", method="POST")
    def reschedule_appointment_for_service_job_by_service_job_id(
        self, serviceJobId, **kwargs
    ) -> ApiResponse:
        """
        reschedule_appointment_for_service_job_by_service_job_id(self, serviceJobId, **kwargs) -> ApiResponse

        Reschedules an appointment for the service job indicated by the service job identifier you specify.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       20
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            serviceJobId:string | * REQUIRED An Amazon defined service job identifier.
            appointmentId:string | * REQUIRED An existing appointment identifier for the Service Job.
            kwargs: Example | >>>
                {
                    "appointmentTime": {
                        "startTime": "2019-08-24T14:15:22Z",
                        "durationInMinutes": 0
                    },
                    "rescheduleReasonCode": "string"
                }

        Returns:
            ApiResponse:
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), serviceJobId), data=kwargs
        )






    @sp_endpoint("/service/v1/serviceJobs/{}/appointments/{}", method="POST")
    def reschedule_appointment_for_service_job_by_service_job_id_post(self, serviceJobId, appointmentId, **kwargs) -> ApiResponse:
        """
        reschedule_appointment_for_service_job_by_service_job_id_post(self, serviceJobId, appointmentId, **kwargs) -> ApiResponse

        Reschedules an appointment for the service job indicated by the service job identifier specified.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            serviceJobId:string | * REQUIRED An Amazon defined service job identifier.
            appointmentId:string | * REQUIRED An existing appointment identifier for the Service Job.
            body:RescheduleAppointmentRequest | * REQUIRED {'description': 'Input for rescheduled appointment operation.',
             'properties': {'appointmentTime': {'$ref': '#/definitions/AppointmentTimeInput', 'description': 'Input appointment time details.'},
                            'rescheduleReasonCode': {'$ref': '#/definitions/RescheduleReasonCode', 'description': 'Input appointment reschedule reason.'}},
             'required': ['appointmentTime', 'rescheduleReasonCode'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), serviceJobId, appointmentId), data=kwargs)

    @sp_endpoint("/service/v1/serviceJobs/{}/appointments/{}/resources", method="PUT")
    def assign_appointment_resources(self, serviceJobId, appointmentId, **kwargs) -> ApiResponse:
        """
        assign_appointment_resources(self, serviceJobId, appointmentId, **kwargs) -> ApiResponse

        Assigns new resource(s) or overwrite/update the existing one(s) to a service job appointment.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 2 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            serviceJobId:string | * REQUIRED An Amazon-defined service job identifier. Get this value by calling the `getServiceJobs` operation of the Services API.
            appointmentId:string | * REQUIRED An Amazon-defined identifier of active service job appointment.
            body:AssignAppointmentResourcesRequest | * REQUIRED {'description': 'Request schema for the `assignAppointmentResources` operation.',
             'properties': {'resources': {'$ref': '#/definitions/AppointmentResources', 'description': 'List of resource objects to be assigned.'}},
             'required': ['resources'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), serviceJobId, appointmentId), data=kwargs)

    @sp_endpoint("/service/v1/serviceJobs/{}/appointments/{}/fulfillment", method="PUT")
    def set_appointment_fulfillment_data(self, serviceJobId, appointmentId, **kwargs) -> ApiResponse:
        """
        set_appointment_fulfillment_data(self, serviceJobId, appointmentId, **kwargs) -> ApiResponse

        Updates the appointment fulfillment data related to a given `jobID` and `appointmentID`.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            serviceJobId:string | * REQUIRED An Amazon-defined service job identifier. Get this value by calling the `getServiceJobs` operation of the Services API.
            appointmentId:string | * REQUIRED An Amazon-defined identifier of active service job appointment.
            body:SetAppointmentFulfillmentDataRequest | * REQUIRED {'description': 'Input for set appointment fulfillment data operation.',
             'properties': {'appointmentResources': {'$ref': '#/definitions/AppointmentResources', 'description': 'Resources involved in appointment fulfillment.'},
                            'estimatedArrivalTime': {'$ref': '#/definitions/DateTimeRange', 'description': 'The range of time when the technician is expected to arrive at the fulfillment location.'},
                            'fulfillmentDocuments': {'$ref': '#/definitions/FulfillmentDocuments', 'description': 'Documents specific to appointment fulfillment.'},
                            'fulfillmentTime': {'$ref': '#/definitions/FulfillmentTime', 'description': 'Input appointment time details.'}},
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), serviceJobId, appointmentId), data=kwargs)

    @sp_endpoint("/service/v1/serviceResources/{}/capacity/range", method="POST")
    def get_range_slot_capacity(self, resourceId, **kwargs) -> ApiResponse:
        """
        get_range_slot_capacity(self, resourceId, **kwargs) -> ApiResponse

        Provides capacity slots in a format similar to availability records.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            resourceId:string | * REQUIRED Resource Identifier.
            body:RangeSlotCapacityQuery | * REQUIRED {'description': 'Request schema for the `getRangeSlotCapacity` operation. This schema is used to define the time range and capacity types that are being queried.',
             'properties': {'capacityTypes': {'description': 'An array of capacity types which are being requested. Default value is `[SCHEDULED_CAPACITY]`.', 'items': {'$ref': '#/definitions/CapacityType'}, 'type': 'array'},
                            'endDateTime': {'description': 'End date time up to which the capacity slots are being requested in ISO 8601 format.', 'format': 'date-time', 'type': 'string'},
                            'startDateTime': {'description': 'Start date time from which the capacity slots are being requested in ISO 8601 format.', 'format': 'date-time', 'type': 'string'}},
             'required': ['startDateTime', 'endDateTime'],
             'type': 'object'}
            key marketplaceIds:array | * REQUIRED An identifier for the marketplace in which the resource operates.
            key nextPageToken:string |  Next page token returned in the response of your previous request.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), resourceId), data=kwargs)

    @sp_endpoint("/service/v1/serviceResources/{}/capacity/fixed", method="POST")
    def get_fixed_slot_capacity(self, resourceId, **kwargs) -> ApiResponse:
        """
        get_fixed_slot_capacity(self, resourceId, **kwargs) -> ApiResponse

        Provides capacity in fixed-size slots. 
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            resourceId:string | * REQUIRED Resource Identifier.
            body:FixedSlotCapacityQuery | * REQUIRED {'description': 'Request schema for the `getFixedSlotCapacity` operation. This schema is used to define the time range, capacity types and slot duration which are being queried.',
             'properties': {'capacityTypes': {'description': 'An array of capacity types which are being requested. Default value is `[SCHEDULED_CAPACITY]`.', 'items': {'$ref': '#/definitions/CapacityType'}, 'type': 'array'},
                            'endDateTime': {'description': 'End date time up to which the capacity slots are being requested in ISO 8601 format.', 'format': 'date-time', 'type': 'string'},
                            'slotDuration': {'description': 'Size in which slots are being requested. This value should be a multiple of 5 and fall in the range: 5 <= `slotDuration` <= 360.', 'format': 'int32', 'multipleOf': 5, 'type': 'number'},
                            'startDateTime': {'description': 'Start date time from which the capacity slots are being requested in ISO 8601 format.', 'format': 'date-time', 'type': 'string'}},
             'required': ['startDateTime', 'endDateTime'],
             'type': 'object'}
            key marketplaceIds:array | * REQUIRED An identifier for the marketplace in which the resource operates.
            key nextPageToken:string |  Next page token returned in the response of your previous request.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), resourceId), data=kwargs)

    @sp_endpoint("/service/v1/serviceResources/{}/schedules", method="PUT")
    def update_schedule(self, resourceId, **kwargs) -> ApiResponse:
        """
        update_schedule(self, resourceId, **kwargs) -> ApiResponse

        Update the schedule of the given resource.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            resourceId:string | * REQUIRED Resource (store) Identifier
            body:UpdateScheduleRequest | * REQUIRED {'description': 'Request schema for the `updateSchedule` operation.',
             'properties': {'schedules': {'$ref': '#/definitions/AvailabilityRecords', 'description': 'List of schedule objects to define the normal working hours of a resource.'}},
             'required': ['schedules'],
             'type': 'object'}
            key marketplaceIds:array | * REQUIRED An identifier for the marketplace in which the resource operates.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), resourceId), data=kwargs)

    @sp_endpoint("/service/v1/reservation", method="POST")
    def create_reservation(self, **kwargs) -> ApiResponse:
        """
        create_reservation(self, **kwargs) -> ApiResponse

        Create a reservation.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            body:CreateReservationRequest | * REQUIRED {'description': 'Request schema for the `createReservation` operation.',
             'properties': {'reservation': {'$ref': '#/definitions/Reservation', 'description': '`Reservation` object to reduce the capacity of a resource.'}, 'resourceId': {'description': 'Resource (store) identifier.', 'type': 'string'}},
             'required': ['reservation', 'resourceId'],
             'type': 'object'}
            key marketplaceIds:array | * REQUIRED An identifier for the marketplace in which the resource operates.

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/service/v1/reservation/{}", method="PUT")
    def update_reservation(self, reservationId, **kwargs) -> ApiResponse:
        """
        update_reservation(self, reservationId, **kwargs) -> ApiResponse

        Update a reservation.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            reservationId:string | * REQUIRED Reservation Identifier
            body:UpdateReservationRequest | * REQUIRED {'description': 'Request schema for the `updateReservation` operation.',
             'properties': {'reservation': {'$ref': '#/definitions/Reservation', 'description': '`Reservation` object to reduce the capacity of a resource.'}, 'resourceId': {'description': 'Resource (store) identifier.', 'type': 'string'}},
             'required': ['reservation', 'resourceId'],
             'type': 'object'}
            key marketplaceIds:array | * REQUIRED An identifier for the marketplace in which the resource operates.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), reservationId), data=kwargs)

    @sp_endpoint("/service/v1/reservation/{}", method="DELETE")
    def cancel_reservation(self, reservationId, **kwargs) -> ApiResponse:
        """
        cancel_reservation(self, reservationId, **kwargs) -> ApiResponse

        Cancel a reservation. 
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            reservationId:string | * REQUIRED Reservation Identifier
            key marketplaceIds:array | * REQUIRED An identifier for the marketplace in which the resource operates.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), reservationId), params=kwargs)

    @sp_endpoint("/service/v1/serviceJobs/{}/appointmentSlots", method="GET")
    def get_appointmment_slots_by_job_id(self, serviceJobId, **kwargs) -> ApiResponse:
        """
        get_appointmment_slots_by_job_id(self, serviceJobId, **kwargs) -> ApiResponse

        Gets appointment slots for the service associated with the service job id specified.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            serviceJobId:string | * REQUIRED A service job identifier to retrive appointment slots for associated service.
            key marketplaceIds:array | * REQUIRED An identifier for the marketplace in which the resource operates.
            key startTime:string |  A time from which the appointment slots will be retrieved. The specified time must be in ISO 8601 format. If `startTime` is provided, `endTime` should also be provided. Default value is as per business configuration.
            key endTime:string |  A time up to which the appointment slots will be retrieved. The specified time must be in ISO 8601 format. If `endTime` is provided, `startTime` should also be provided. Default value is as per business configuration. Maximum range of appointment slots can be 90 days.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), serviceJobId), params=kwargs)

    @sp_endpoint("/service/v1/appointmentSlots", method="GET")
    def get_appointment_slots(self, **kwargs) -> ApiResponse:
        """
        get_appointment_slots(self, **kwargs) -> ApiResponse

        Gets appointment slots as per the service context specified.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 20 | 40 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            key asin:string | * REQUIRED ASIN associated with the service.
            key storeId:string | * REQUIRED Store identifier defining the region scope to retrive appointment slots.
            key marketplaceIds:array | * REQUIRED An identifier for the marketplace for which appointment slots are queried
            key startTime:string |  A time from which the appointment slots will be retrieved. The specified time must be in ISO 8601 format. If `startTime` is provided, `endTime` should also be provided. Default value is as per business configuration.
            key endTime:string |  A time up to which the appointment slots will be retrieved. The specified time must be in ISO 8601 format. If `endTime` is provided, `startTime` should also be provided. Default value is as per business configuration. Maximum range of appointment slots can be 90 days.

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/service/v1/documents", method="POST")
    def create_service_document_upload_destination(self, **kwargs) -> ApiResponse:
        """
        create_service_document_upload_destination(self, **kwargs) -> ApiResponse

        Creates an upload destination.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            body:ServiceUploadDocument | * REQUIRED {'description': 'Input for to be uploaded document.',
             'properties': {'contentLength': {'description': 'The content length of the to-be-uploaded file', 'format': 'int64', 'maximum': 5242880, 'minimum': 1, 'type': 'number'},
                            'contentMD5': {'description': 'An MD5 hash of the content to be submitted to the upload destination. This value is used to determine if the data has been corrupted or tampered with during transit.',
                                           'pattern': '^[A-Za-z0-9\\\\+/]{22}={2}$',
                                           'type': 'string'},
                            'contentType': {'description': 'The content type of the to-be-uploaded file',
                                            'enum': ['TIFF', 'JPG', 'PNG', 'JPEG', 'GIF', 'PDF'],
                                            'type': 'string',
                                            'x-docgen-enum-table-extension': [{'description': 'To be uploaded POA is of type image/tiff.', 'value': 'TIFF'},
                                                                              {'description': 'To be uploaded POA is of type image/jpg.', 'value': 'JPG'},
                                                                              {'description': 'To be uploaded POA is of type image/png.', 'value': 'PNG'},
                                                                              {'description': 'To be uploaded POA is of type image/jpeg.', 'value': 'JPEG'},
                                                                              {'description': 'To be uploaded POA is of type image/gif.', 'value': 'GIF'},
                                                                              {'description': 'To be uploaded POA is of type application/pdf.', 'value': 'PDF'}]}},
             'required': ['contentLength', 'contentType'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs)

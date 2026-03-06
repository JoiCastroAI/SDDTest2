import React, { useState, useEffect, useMemo } from 'react';
import { Form, Row, Col } from 'react-bootstrap';
import type { CreateCompanyRequest, Company } from '../../types/company';

type CompanyFormProps = {
    initialData?: Company;
    onSubmit: (data: CreateCompanyRequest) => void;
    formId: string;
};

const emptyForm: CreateCompanyRequest = {
    name: '',
    street: '',
    city: '',
    state: '',
    zip_code: '',
    country: '',
    billing: 0,
    expenses: 0,
    employees: 0,
    clients: 0,
};

const CompanyForm: React.FC<CompanyFormProps> = ({ initialData, onSubmit, formId }) => {
    const [formData, setFormData] = useState<CreateCompanyRequest>(emptyForm);
    const [validated, setValidated] = useState(false);

    useEffect(() => {
        if (initialData) {
            setFormData({
                name: initialData.name,
                street: initialData.street,
                city: initialData.city,
                state: initialData.state,
                zip_code: initialData.zip_code,
                country: initialData.country,
                billing: initialData.billing,
                expenses: initialData.expenses,
                employees: initialData.employees,
                clients: initialData.clients,
            });
        }
    }, [initialData]);

    const profit = useMemo(() => formData.billing - formData.expenses, [formData.billing, formData.expenses]);

    const formatCurrency = (value: number): string => {
        if (Math.abs(value) >= 1_000_000) {
            return `$${(value / 1_000_000).toFixed(2)}M`;
        }
        return `$${value.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
    };

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value, type } = e.target;
        setFormData((prev) => ({
            ...prev,
            [name]: type === 'number' ? Number(value) || 0 : value,
        }));
    };

    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const form = e.currentTarget;
        if (!form.checkValidity()) {
            setValidated(true);
            return;
        }
        onSubmit(formData);
    };

    return (
        <Form
            id={formId}
            className="company-form"
            noValidate
            validated={validated}
            onSubmit={handleSubmit}
        >
            <h3 className="form-section-title">Basic Info</h3>
            <Form.Group className="mb-4">
                <Form.Label>
                    Company Name <span className="required-asterisk">*</span>
                </Form.Label>
                <Form.Control
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    placeholder="E.g.: TechVision Solutions"
                    required
                />
                <Form.Control.Feedback type="invalid">Name is required.</Form.Control.Feedback>
            </Form.Group>

            <h3 className="form-section-title">Address</h3>
            <Form.Group className="mb-3">
                <Form.Label>
                    Street <span className="required-asterisk">*</span>
                </Form.Label>
                <Form.Control
                    type="text"
                    name="street"
                    value={formData.street}
                    onChange={handleChange}
                    placeholder="E.g.: 123 Main Street"
                    required
                />
                <Form.Control.Feedback type="invalid">Street is required.</Form.Control.Feedback>
            </Form.Group>
            <Row className="mb-3">
                <Col>
                    <Form.Group>
                        <Form.Label>
                            City <span className="required-asterisk">*</span>
                        </Form.Label>
                        <Form.Control
                            type="text"
                            name="city"
                            value={formData.city}
                            onChange={handleChange}
                            placeholder="E.g.: San Francisco"
                            required
                        />
                        <Form.Control.Feedback type="invalid">City is required.</Form.Control.Feedback>
                    </Form.Group>
                </Col>
                <Col>
                    <Form.Group>
                        <Form.Label>
                            State <span className="required-asterisk">*</span>
                        </Form.Label>
                        <Form.Control
                            type="text"
                            name="state"
                            value={formData.state}
                            onChange={handleChange}
                            placeholder="E.g.: CA"
                            required
                        />
                        <Form.Control.Feedback type="invalid">State is required.</Form.Control.Feedback>
                    </Form.Group>
                </Col>
            </Row>
            <Row className="mb-4">
                <Col>
                    <Form.Group>
                        <Form.Label>
                            Zip Code <span className="required-asterisk">*</span>
                        </Form.Label>
                        <Form.Control
                            type="text"
                            name="zip_code"
                            value={formData.zip_code}
                            onChange={handleChange}
                            placeholder="E.g.: 94102"
                            required
                        />
                        <Form.Control.Feedback type="invalid">Zip code is required.</Form.Control.Feedback>
                    </Form.Group>
                </Col>
                <Col>
                    <Form.Group>
                        <Form.Label>
                            Country <span className="required-asterisk">*</span>
                        </Form.Label>
                        <Form.Control
                            type="text"
                            name="country"
                            value={formData.country}
                            onChange={handleChange}
                            placeholder="E.g.: USA"
                            required
                        />
                        <Form.Control.Feedback type="invalid">Country is required.</Form.Control.Feedback>
                    </Form.Group>
                </Col>
            </Row>

            <h3 className="form-section-title">Financial Data</h3>
            <Row className="mb-3">
                <Col>
                    <Form.Group>
                        <Form.Label>
                            Billing ($) <span className="required-asterisk">*</span>
                        </Form.Label>
                        <Form.Control
                            type="number"
                            name="billing"
                            value={formData.billing}
                            onChange={handleChange}
                            min={0}
                            required
                        />
                    </Form.Group>
                </Col>
                <Col>
                    <Form.Group>
                        <Form.Label>
                            Expenses ($) <span className="required-asterisk">*</span>
                        </Form.Label>
                        <Form.Control
                            type="number"
                            name="expenses"
                            value={formData.expenses}
                            onChange={handleChange}
                            min={0}
                            required
                        />
                    </Form.Group>
                </Col>
            </Row>
            <div className="profit-display mb-4">
                <span className="profit-label">Calculated profit:</span>
                <span className="profit-value">{formatCurrency(profit)}</span>
            </div>

            <h3 className="form-section-title">Other Data</h3>
            <Row className="mb-3">
                <Col>
                    <Form.Group>
                        <Form.Label>
                            Number of Employees <span className="required-asterisk">*</span>
                        </Form.Label>
                        <Form.Control
                            type="number"
                            name="employees"
                            value={formData.employees}
                            onChange={handleChange}
                            min={0}
                            required
                        />
                    </Form.Group>
                </Col>
                <Col>
                    <Form.Group>
                        <Form.Label>
                            Number of Clients <span className="required-asterisk">*</span>
                        </Form.Label>
                        <Form.Control
                            type="number"
                            name="clients"
                            value={formData.clients}
                            onChange={handleChange}
                            min={0}
                            required
                        />
                    </Form.Group>
                </Col>
            </Row>
        </Form>
    );
};

export default CompanyForm;

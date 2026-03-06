import React, { useState, useCallback, useEffect } from 'react';
import { Table, Form, Button, Spinner, Alert, Modal } from 'react-bootstrap';
import { Plus, PencilSquare, Trash, ArrowDownUp } from 'react-bootstrap-icons';
import { useListCompaniesQuery, useDeleteCompanyMutation } from '../features/companies/companiesApi';
import CreateCompanyModal from '../features/companies/CreateCompanyModal';
import EditCompanyModal from '../features/companies/EditCompanyModal';
import type { Company } from '../types/company';

const CompaniesPage: React.FC = () => {
    const [page, setPage] = useState(1);
    const [pageSize] = useState(10);
    const [search, setSearch] = useState('');
    const [debouncedSearch, setDebouncedSearch] = useState('');
    const [sortBy, setSortBy] = useState('name');
    const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('asc');

    const [showCreate, setShowCreate] = useState(false);
    const [showEdit, setShowEdit] = useState(false);
    const [editingCompany, setEditingCompany] = useState<Company | null>(null);

    const [selectedIds, setSelectedIds] = useState<Set<number>>(new Set());
    const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);

    const [deleteCompany] = useDeleteCompanyMutation();

    useEffect(() => {
        const timer = setTimeout(() => {
            setDebouncedSearch(search);
            setPage(1);
        }, 300);
        return () => clearTimeout(timer);
    }, [search]);

    const { data, isLoading, isError, error } = useListCompaniesQuery({
        page,
        page_size: pageSize,
        search: debouncedSearch || undefined,
        sort_by: sortBy,
        sort_order: sortOrder,
    });

    const handleSort = useCallback((column: string) => {
        setSortBy((prev) => {
            if (prev === column) {
                setSortOrder((order) => (order === 'asc' ? 'desc' : 'asc'));
                return prev;
            }
            setSortOrder('asc');
            return column;
        });
    }, []);

    const handleEdit = useCallback((company: Company) => {
        setEditingCompany(company);
        setShowEdit(true);
    }, []);

    const handleSelectRow = useCallback((id: number) => {
        setSelectedIds((prev) => {
            const next = new Set(prev);
            if (next.has(id)) {
                next.delete(id);
            } else {
                next.add(id);
            }
            return next;
        });
    }, []);

    const handleSelectAll = useCallback(() => {
        if (!data) return;
        setSelectedIds((prev) => {
            if (prev.size === data.items.length) {
                return new Set();
            }
            return new Set(data.items.map((c) => c.id));
        });
    }, [data]);

    const handleBulkDelete = async () => {
        for (const id of selectedIds) {
            await deleteCompany(id).unwrap();
        }
        setSelectedIds(new Set());
        setShowDeleteConfirm(false);
    };

    const formatCurrency = (value: number): string => {
        if (Math.abs(value) >= 1_000_000) {
            return `$${(value / 1_000_000).toFixed(2)}M`;
        }
        if (Math.abs(value) >= 1_000) {
            return `$${(value / 1_000).toFixed(1)}K`;
        }
        return `$${value.toFixed(2)}`;
    };

    const renderSortHeader = (label: string, column: string) => (
        <button className="sort-btn" onClick={() => handleSort(column)}>
            {label} <ArrowDownUp size={14} />
        </button>
    );

    return (
        <div>
            <div className="companies-header">
                <div>
                    <h1 className="companies-title">Companies</h1>
                    <p className="companies-subtitle">Manage all companies registered in the system</p>
                </div>
                <div className="d-flex gap-2">
                    {selectedIds.size > 0 && (
                        <Button
                            className="btn-delete-selected"
                            onClick={() => setShowDeleteConfirm(true)}
                        >
                            Delete Selected ({selectedIds.size})
                        </Button>
                    )}
                    <Button className="btn-primary-custom" onClick={() => setShowCreate(true)}>
                        <Plus size={20} /> New Company
                    </Button>
                </div>
            </div>

            <div className="companies-search">
                <div className="search-wrapper">
                    <Form.Control
                        className="search-input"
                        type="text"
                        placeholder="Search companies..."
                        aria-label="Search companies"
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                    />
                </div>
            </div>

            {isLoading && (
                <div className="text-center p-5">
                    <Spinner animation="border" role="status">
                        <span className="visually-hidden">Loading...</span>
                    </Spinner>
                </div>
            )}

            {isError && (
                <div className="px-4">
                    <Alert variant="danger">
                        Failed to load companies.{' '}
                        {error && 'status' in error ? `Error ${error.status}` : 'Please try again.'}
                    </Alert>
                </div>
            )}

            {data && data.items.length === 0 && (
                <div className="px-4">
                    <Alert variant="info">
                        {debouncedSearch
                            ? `No companies found matching "${debouncedSearch}".`
                            : 'No companies registered yet. Create your first company!'}
                    </Alert>
                </div>
            )}

            {data && data.items.length > 0 && (
                <>
                    <div className="companies-table-wrapper">
                        <Table className="companies-table" hover>
                            <thead>
                                <tr>
                                    <th style={{ width: 50 }}>
                                        <Form.Check
                                            type="checkbox"
                                            checked={selectedIds.size === data.items.length}
                                            onChange={handleSelectAll}
                                            aria-label="Select all"
                                        />
                                    </th>
                                    <th>{renderSortHeader('Name', 'name')}</th>
                                    <th>Address</th>
                                    <th className="col-numeric">{renderSortHeader('Billing', 'billing')}</th>
                                    <th className="col-numeric">{renderSortHeader('Expenses', 'expenses')}</th>
                                    <th className="col-numeric">{renderSortHeader('Profit', 'billing')}</th>
                                    <th className="col-numeric">{renderSortHeader('Employees', 'employees')}</th>
                                    <th className="col-numeric">{renderSortHeader('Clients', 'clients')}</th>
                                    <th className="col-actions">Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {data.items.map((company) => (
                                    <tr key={company.id}>
                                        <td>
                                            <Form.Check
                                                type="checkbox"
                                                checked={selectedIds.has(company.id)}
                                                onChange={() => handleSelectRow(company.id)}
                                                aria-label={`Select ${company.name}`}
                                            />
                                        </td>
                                        <td>{company.name}</td>
                                        <td className="col-address">
                                            {company.city}, {company.state}
                                        </td>
                                        <td className="col-numeric">{formatCurrency(company.billing)}</td>
                                        <td className="col-numeric">{formatCurrency(company.expenses)}</td>
                                        <td className="col-numeric col-profit">
                                            {formatCurrency(company.profit)}
                                        </td>
                                        <td className="col-numeric">{company.employees}</td>
                                        <td className="col-numeric">{company.clients}</td>
                                        <td className="col-actions">
                                            <button
                                                className="action-btn"
                                                onClick={() => handleEdit(company)}
                                                aria-label={`Edit ${company.name}`}
                                            >
                                                <PencilSquare size={16} />
                                            </button>
                                            <button
                                                className="action-btn action-btn-delete"
                                                onClick={() => {
                                                    setSelectedIds(new Set([company.id]));
                                                    setShowDeleteConfirm(true);
                                                }}
                                                aria-label={`Delete ${company.name}`}
                                            >
                                                <Trash size={16} />
                                            </button>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </Table>
                    </div>

                    <div className="companies-footer d-flex justify-content-between align-items-center">
                        <span>
                            Showing {data.items.length} of {data.total} companies
                        </span>
                        {data.total_pages > 1 && (
                            <div className="pagination-controls">
                                <Button
                                    variant="outline-secondary"
                                    size="sm"
                                    disabled={page <= 1}
                                    onClick={() => setPage((p) => p - 1)}
                                >
                                    Previous
                                </Button>
                                <span>
                                    Page {data.page} of {data.total_pages}
                                </span>
                                <Button
                                    variant="outline-secondary"
                                    size="sm"
                                    disabled={page >= data.total_pages}
                                    onClick={() => setPage((p) => p + 1)}
                                >
                                    Next
                                </Button>
                            </div>
                        )}
                    </div>
                </>
            )}

            <CreateCompanyModal show={showCreate} onHide={() => setShowCreate(false)} />
            <EditCompanyModal
                show={showEdit}
                onHide={() => {
                    setShowEdit(false);
                    setEditingCompany(null);
                }}
                company={editingCompany}
            />

            <Modal show={showDeleteConfirm} onHide={() => setShowDeleteConfirm(false)} centered>
                <Modal.Header closeButton>
                    <Modal.Title>Confirm Delete</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    Are you sure you want to delete {selectedIds.size} company
                    {selectedIds.size > 1 ? 'ies' : 'y'}? This action cannot be undone.
                </Modal.Body>
                <Modal.Footer>
                    <Button className="btn-cancel" onClick={() => setShowDeleteConfirm(false)}>
                        Cancel
                    </Button>
                    <Button className="btn-delete-selected" onClick={handleBulkDelete}>
                        Delete
                    </Button>
                </Modal.Footer>
            </Modal>
        </div>
    );
};

export default CompaniesPage;
